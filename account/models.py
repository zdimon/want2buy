# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.contrib.auth import authenticate, login
from django.dispatch import receiver
from registration.signals import user_activated

@receiver(user_activated)
def login_on_activation(sender, user, request, **kwargs):
    print 'dddddddddddddddddddddddddddd %s' % user
    """Logs in the user after activation"""
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)

class Profile(models.Model):
    user=models.OneToOneField(User, primary_key=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    middle_name = models.CharField(_('middle name'), max_length=50, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone = models.CharField(_('phone'), max_length=50, blank=True)
    site = models.URLField(_('site'), max_length=50, blank=True)
    address = models.CharField(_('address'), max_length=150, blank=True)
    rating = models.IntegerField(default=0)
    account = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    #USERNAME_FIELD = 'email'
    #objects = MyUserManager()

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = Profile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User)     

class Testimonial(models.Model):
    author = models.ForeignKey(Profile)
    content = models.TextField()
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

class Transaction(models.Model):
    user = models.ForeignKey(Profile)
    ammount = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)    