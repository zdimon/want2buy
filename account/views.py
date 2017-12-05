# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from registration.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail
from account.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import redirect
from registration.backends.hmac.views import RegistrationView, ActivationView
from registration import signals
from django.contrib.auth import authenticate, login
from registration.signals import user_activated
from registration.models import RegistrationProfile
# Create your views here.

class ProfileForm(RegistrationFormUniqueEmail):
    def __init__(self, *args, **kwargs):
        super(RegistrationFormUniqueEmail,self).__init__(*args, **kwargs)
        del self.fields['username']

class MyRegistrationView(RegistrationView):
    form_class = ProfileForm
    def register(self, form):
        #p = self.create_inactive_user(form)
        
        #print self.get_activation_key(p)

        p = User()
        p.username = form.cleaned_data['email']
        p.email = form.cleaned_data['email']
        p.set_password(form.cleaned_data['password1'])
        p.is_active = False
        p.save()
        RegistrationProfile.objects.create_profile(p)

        signals.user_registered.send(sender=self.__class__,
                                     user=p,
                                     request=self.request)
        self.send_activation_email(p)
        return p

    def get_success_url(self, user):
        return ('registration_done', (), {})

class MyActivationView(ActivationView):   
    success_url = 'activation_done'
    def activate(self, *args, **kwargs):
        #import pdb; pdb.set_trace()
        username = self.validate_key(kwargs.get('activation_key'))
        if username is not None:
            user = self.get_user(username)
            if user is not None:
                user.is_active = True
                user.save()
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(self.request, user)
                #return redirect('profile_edit')
                return user
        return False

def profile_edit(request):
    return render(request, 'account/profile_edit.html')


def registration_done(request):
    return render(request, 'account/registration_done.html')

def activation_done(request):
    return render(request, 'account/activate.html')