from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from forms import *
from django.shortcuts import render, redirect
from main.models import Feedback


def feedback(request):
    logined = request.user.is_authenticated()
    if request.method == 'POST':
        if logined:
            form = ContactForm(request.POST, logined=True)
        else:
            form = ContactForm(request.POST, logined=False)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            f = Feedback()
            f.subject = subject
            f.message = message
            if not logined:
                sender = form.cleaned_data['sender']
                f.email = sender
            else:
                f.user = request.user.profile
            f.save()
            return redirect(postFeedback)
    else:
        if request.user.is_authenticated():
            form = ContactForm(logined=True)
        else:
            form = ContactForm(logined=False)
        return render(request, 'feedback.html', {'form': form})


def postFeedback(request):
    return render(request, 'feedback1.html')
