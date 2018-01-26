from django import forms
from registration.models import RegistrationProfile
from django.contrib.auth.models import User
from registration.backends.hmac.views import RegistrationView
import random
from registration import signals
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
REGISTRATION_SALT = getattr(settings, 'REGISTRATION_SALT', 'registration')
from django.core import signing
from archive.models import Offer, OfferMessage, Announcement
from account.models import Profile
from want2buy.settings import BASE_DIR
from django.core.files import File

def save_offer(data):
    an = Announcement.objects.get(pk=data['announcement_id'])
    seller = User.objects.get(pk=data['user_id'])
    try:
        o = Offer.objects.get(announcement=an,seller=seller)
    except:
        o = Offer()
    o.price = data['price']
    o.announcement = an
    o.seller = seller
    o.buyer = an.user
    o.save()
    m = OfferMessage()
    m.offer = o
    m.message = data['desc']
    m.new_price = data['price']
    m.user = seller
    m.save()
    return o

class OfferForm(forms.Form):
    desc = forms.CharField(widget=forms.Textarea, required=True)
    username = forms.CharField()
    price = forms.CharField(required=True)
    url = forms.CharField(required=False)
    email = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    file = forms.FileField(required=False)
    announcement_id = forms.CharField(widget=forms.HiddenInput)


    email_body_template = 'registration/activation_email.txt'
    email_subject_template = 'registration/activation_email_subject.txt'


    def get_email_context(self, activation_key, request):
        """
        Build the template context used for the activation email.

        """
        return {
            'activation_key': activation_key,
            'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
            'site': get_current_site(request)
        }    

    def get_activation_key(self, user):
        """
        Generate the activation key which will be emailed to the user.

        """
        return signing.dumps(
            obj=getattr(user, user.USERNAME_FIELD),
            salt=REGISTRATION_SALT
        )

    def send_activation_email(self, user, request):
        """
        Send the activation email. The activation key is the username,
        signed using TimestampSigner.

        """
        activation_key = self.get_activation_key(user)
        context = self.get_email_context(activation_key,request)
        context.update({
            'user': user
        })
        subject = render_to_string(self.email_subject_template,
                                   context)
        # Force subject to a single line to avoid header-injection
        # issues.
        subject = ''.join(subject.splitlines())
        message = render_to_string(self.email_body_template,
                                   context)
        user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

    def handle_uploaded_file(self,f,offer):
        path = '%s/tmp/%s.jpg' % (BASE_DIR, offer.id)
        with open(path, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return path

    def save(self,request):
        data = self.cleaned_data
        if not request.user.is_authenticated():
            passwd = random.randint(1111,9999)
            p = User()
            p.username = data['email']
            p.email = data['email']
            p.set_password(passwd)
            p.is_active = False
            p.first_name = data['username']
            p.save()
            RegistrationProfile.objects.create_profile(p)

            signals.user_registered.send(sender=self.__class__,
                                        user=p,
                                        request=request)
            
            profile = Profile.objects.get(user_id=p.id)
            profile.first_name = data['username']
            profile.save()

            self.send_activation_email(p,request)
            data['user_id'] = p.id
        else:
            data['user_id'] = request.user.id
        m = save_offer(data)
        try:
            if request.FILES['file']:
                name = '%s.jpg' % (m.id,)
                path = self.handle_uploaded_file(request.FILES['file'], m)
                m.file.save(
                    name,
                    File(open(path))
                    )  
        except:
            pass
        return data