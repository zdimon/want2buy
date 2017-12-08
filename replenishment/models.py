# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from account.models import Profile
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Replanishment(models.Model):
    Visa = 'VS',
    MasterCard = 'MC',
    WebMoney = 'WM',
    Replanishment_system_choices = (
        (Visa, 'Visa'),
        (MasterCard, 'MasterCard'),
        (WebMoney, 'WebMoney'),
    )
    Replanishment_system = models.CharField(verbose_name='платежная система', max_length=150, choices=Replanishment_system_choices, default=MasterCard)
    user_replanishment = models.ForeignKey(User)
    ammount = models.FloatField(verbose_name='сумма')
    created_at = models.DateTimeField(default=timezone.now())


