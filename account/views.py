# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from registration.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail
from account.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Create your views here.

class ProfileForm(RegistrationFormUniqueEmail):
    def __init__(self, *args, **kwargs):
        super(RegistrationFormUniqueEmail,self).__init__(*args, **kwargs)
        del self.fields['username']

class MyRegistrationView(RegistrationView):
    form_class = ProfileForm() 
    success_url = '/profile/'
    def register(self, form):
        print form.cleaned_data['email']

        p = User()
        p.username = form.cleaned_data['email']
        p.email = form.cleaned_data['email']
        p.set_password(form.cleaned_data['password1'])
        p.save()
        print p  
        return p

    def form_valid(self, form):
        new_user = self.register(form)
        
        return redirect('/profile/')