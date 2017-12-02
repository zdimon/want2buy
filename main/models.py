# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    alias = models.CharField(max_length=150)
    meta_title = models.CharField(max_length=150)
    meta_keywords = models.CharField(max_length=250)
    meta_description = models.CharField(max_length=250)


class Category(models.Model):
    name = models.CharField(max_length=150)


class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    parent_category = models.ForeignKey(Category)
    url = models.URLField()
