# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Profile
# Create your models here.


class Replanishment(models.Model):
    status_choices = (
        ('pending', _('В обработке ')),
        ('success', _('Подтвержден')),
        ('failure', _('Отклонен')),
        ('error', _('Ошибка')),
        ('sandbox', _('Тест'))
    )

    user_replanishment = models.ForeignKey('account.Profile')
    amount = models.FloatField(verbose_name='сумма')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    status = models.CharField(max_length=100, choices=status_choices, default='pending', verbose_name='Статус')

