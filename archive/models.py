# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from catalog.models import *
from image_cropping import ImageRatioField
from image_cropping.utils import get_backend


# Create your models here.


class AnnouncementBase(models.Model):
    new = (
        ('new', _('Новое')),
        ('used', _('БУ')),
    )

    opt = (
        ('opt', _('Опт')),
        ('retail', _('Розница')),
    )

    user = models.ForeignKey(User)
    title = models.TextField()
    category = models.ForeignKey(SubSubCategory)
    new_category = models.TextField()
    new_bu = models.CharField(max_length=10, choices=new)
    opt_roznica = models.CharField(max_length=10, choices=opt)
    price = models.FloatField()
    ammount = models.IntegerField()
    city = models.ForeignKey(City)
    info = models.TextField
    photo = models.ImageField(upload_to='new_announcements/', null=True, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    cropping = ImageRatioField('photo', '150x150')

    def __unicode__(self):
        return self.title

    def full_category(self):
        return '%s->%s->%s' % (self.category.parent_sub_category.parent_category, \
                               self.category.parent_sub_category, \
                               self.category \
                               )

    def thumbnail(self):
        thumbnail_url = get_backend().get_thumbnail_url(
            self.photo,
            {
                'size': (100, 100),
                'box': self.cropping,
                'crop': True,
                'detail': True,
            }
        )
        return '<img src="%s"  />' % thumbnail_url

    thumbnail.allow_tags = True

    class Meta:
        abstract = True


class NewAnnouncement(AnnouncementBase):
    pass


class Announcement(AnnouncementBase):
    is_paid = models.BooleanField(default=False)
