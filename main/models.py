# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse


# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    alias = models.CharField(max_length=150)
    meta_title = models.CharField(max_length=150)
    meta_keywords = models.CharField(max_length=250)
    meta_description = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('show_page', kwargs={'alias': self.alias})