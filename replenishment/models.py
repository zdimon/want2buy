# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from account.models import Profile
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Replanishment(models.Model):

    Replanishment_system_choices = (
        ('VS', 'Visa'),
        ('MC', 'MasterCard'),
        ('WM', 'WebMoney'),
    )
    
    Replanishment_system = models.CharField(verbose_name='платежная система', max_length=150, choices=Replanishment_system_choices, default='VS')
    user_replanishment = models.ForeignKey(User)
    ammount = models.FloatField(verbose_name='сумма')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)


