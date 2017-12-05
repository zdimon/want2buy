from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from forms import *
from django.shortcuts import render


def feedback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']

            recipients = ['myemail@gmail.com']
            try:
                send_mail(subject, message, sender, recipients)
                return render(request, '_feedback.html')
            except BadHeaderError:
                return HttpResponse('Invalid header found')

    else:
        form = ContactForm()
    return render(request, 'feedback.html', {'form': form})
