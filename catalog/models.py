# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from slugify import slugify
from image_cropping import ImageRatioField
from image_cropping.utils import get_backend
from django.utils.text import ugettext_lazy as _


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name=_(u'Название'))
    name_slug = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='catalog_pic/', null=True, blank=True, verbose_name=_(u'Фото'))
    cropping = ImageRatioField('photo', '255x200', verbose_name=_(u'Кадрирование'))

    def get_absolute_url(self):
        return reverse('catalog_main', kwargs={'slug': self.name_slug})

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def thumbnail(self):
        try:
            thumbnail_url = get_backend().get_thumbnail_url(
                self.photo,
                {
                    'size': (255, 200),
                    'box': self.cropping,
                    'crop': True,
                    'detail': True,
                }
            )
            return '<img class="img-responsive" src="%s"  />' % thumbnail_url
        except:
            return '<img class="img-responsive" src="/static/images/noimage.png" />'

    thumbnail.allow_tags = True


class SubCategory(models.Model):
    name = models.CharField(max_length=150, verbose_name=_(u'Название'))
    parent_category = models.ForeignKey(Category, verbose_name=_(u'Базовая категория'))
    name_slug = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse('catalog_sub', kwargs={'slug': self.name_slug})

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)


class SubSubCategory(models.Model):
    name = models.CharField(max_length=150, verbose_name=_(u'Название'))
    parent_sub_category = models.ForeignKey(SubCategory, verbose_name=_(u'Базовая подкатегория'))
    name_slug = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse('catalog_sub_sub', kwargs={'slug': self.name_slug})

    @property
    def parent_category(self):
        return self.parent_sub_category.parent_category

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(SubSubCategory, self).save(*args, **kwargs)


class Region(models.Model):
    name = models.CharField(max_length=150, verbose_name=_(u'Название'))
    name_slug = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Region, self).save(*args, **kwargs)


class City(models.Model):
    name = models.CharField(max_length=150, verbose_name=_(u'Название'))
    region = models.ForeignKey(Region, verbose_name=_(u'Регион'))
    lat = models.FloatField()
    lon = models.FloatField()

    name_slug = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)
