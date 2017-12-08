# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from slugify import slugify


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    name_slug = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    parent_category = models.ForeignKey(Category)
    name_slug = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)


class SubSubCategory(models.Model):
    name = models.CharField(max_length=150)
    parent_sub_category = models.ForeignKey(SubCategory)
    name_slug = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(SubSubCategory, self).save(*args, **kwargs)

class Region(models.Model):
    name = models.CharField(max_length=150)
    name_slug = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Region, self).save(*args, **kwargs)


class City(models.Model):
    name = models.CharField(max_length=150)
    region = models.ForeignKey(Region)
    lat = models.FloatField()
    lon = models.FloatField()

    name_slug = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)