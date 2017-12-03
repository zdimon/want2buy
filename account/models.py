# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

from django.contrib.auth.base_user import AbstractBaseUser

class Profile(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
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
    USERNAME_FIELD = 'email'


class Testimonial(models.Model):
    author = models.ForeignKey(Profile)
    content = models.TextField()
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

class Transaction(models.Model):
    user = models.ForeignKey(Profile)
    ammount = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)    