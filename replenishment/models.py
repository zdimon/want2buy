# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from account.models import Profile
from django.utils import timezone

# Create your models here.


class Replanishment(models.Model):
    user_replanishment = models.ForeignKey(Profile.user)
    ammount = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now())
    system = models.CharField(max_length=150)

