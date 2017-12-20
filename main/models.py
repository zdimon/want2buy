# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse
from django.utils.text import ugettext_lazy as _


# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=150, verbose_name=_(u'Заголовок'))
    content = models.TextField(verbose_name=_(u'Содержание'))
    alias = models.CharField(max_length=150, verbose_name=_(u'Алиас'))
    meta_title = models.CharField(max_length=150, verbose_name=_(u'Мета-заголовок'))
    meta_keywords = models.CharField(max_length=250, verbose_name=_(u'Мета-словосочитания'))
    meta_description = models.CharField(max_length=250, verbose_name=_(u'Мета-описание'))

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_page', kwargs={'alias': self.alias})


class Feedback(models.Model):
    subject = models.TextField(max_length=100, verbose_name=_(u'Тема'))
    email = models.TextField(null=True, blank=True, verbose_name=_(u'E-mail'))
    user = models.ForeignKey('account.Profile', null=True, blank=True, verbose_name=_(u'Пользователь'))
    message = models.TextField(verbose_name=_(u'Сообщнеие'))
    resolved = models.BooleanField(default=False, verbose_name=_(u'Статус'))
