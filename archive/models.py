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

    tp = (
        ('service', _('Услуга')),
        ('good', _('Товар')),
    )

    once = (
        ('once', _('Одноразовая покупка')),
        ('regular', _('Постоянно требуется')),
    )

    user = models.ForeignKey(User)
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, null=True, blank=True)
    sub_sub_category = models.ForeignKey(SubSubCategory, null=True, blank=True)
    new_category = models.CharField(max_length=250, null=True, blank=True)
    new_bu = models.CharField(max_length=10, choices=new, default='new')
    opt_roznica = models.CharField(max_length=10, choices=opt, default='retail')
    type = models.CharField(max_length=10, choices=tp, default='good')
    once = models.CharField(max_length=10, choices=once, default='once')
    price = models.FloatField()
    ammount = models.IntegerField(default=1)
    city = models.ForeignKey(City, null=True, blank=True)
    region = models.ForeignKey(Region, null=True, blank=True)
    new_city = models.CharField(max_length=250, null=True, blank=True)
    info = models.TextField
    photo = models.ImageField(upload_to='new_announcements/', null=True, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    cropping = ImageRatioField('photo', '150x150')
    is_paid = models.BooleanField(default=False)
    date_expire = models.DateField(_('Date expire'), null=True, blank=True)
    date_paid_expire = models.DateField(_('Date paid expire'), null=True, blank=True)
    
    def __unicode__(self):
        return self.title

    def full_category(self):
        return '%s->%s->%s' % (self.category.parent_sub_category.parent_category, \
                               self.category.parent_sub_category, \
                               self.category \
                               )

    def thumbnail(self):
        try:
            thumbnail_url = get_backend().get_thumbnail_url(
                self.photo,
                {
                    'size': (100, 100),
                    'box': self.cropping,
                    'crop': True,
                    'detail': True,
                }
            )
            return '<img class="img-responsive" src="%s"  />' % thumbnail_url
        except:
            return '<img class="img-responsive" src="/static/images/noimage.png" />'

    thumbnail.allow_tags = True

    class Meta:
        abstract = True


class NewAnnouncement(AnnouncementBase):
    pass


class Announcement(AnnouncementBase):
    pass

