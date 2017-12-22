# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Profile
from django.contrib.auth.models import User
# Create your models here.


class Replanishment(models.Model):
    status_choices = (
        ('pending', _('В обработке ')),
        ('success', _('Подтвержден')),
        ('failure', _('Отклонен')),
        ('error', _('Ошибка')),
        ('sandbox', _('Тест'))
    )

    Replanishment_system_choices =  (
        ('liqpay', _('Ликпей')),
        
    )
    
    Replanishment_system = models.CharField(verbose_name=_('платежная система'), max_length=150, choices=Replanishment_system_choices, default='liqpay')
    user_replanishment = models.ForeignKey(User)
    ammount = models.FloatField(verbose_name=_('сумма'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_(u'Дата создани'))
    status = models.CharField(max_length=100, choices=status_choices, default='pending', verbose_name='Статус')
    
