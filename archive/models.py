# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from catalog.models import *
from image_cropping import ImageRatioField
from image_cropping.utils import get_backend
from django.core.urlresolvers import reverse

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
    price = models.DecimalField(verbose_name=_(u'Цена'), max_digits=19, decimal_places=2)
    ammount = models.IntegerField(default=1)
    city = models.ForeignKey(City, null=True, blank=True)
    region = models.ForeignKey(Region, null=True, blank=True)
    new_city = models.CharField(max_length=250, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='announcements/', null=True, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    cropping = ImageRatioField('photo', '150x150')
    is_paid = models.BooleanField(default=False)
    date_expire = models.DateField(_('Date expire'), null=True, blank=True)
    date_paid_expire = models.DateField(_('Date paid expire'), null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('annoncement_detail', kwargs={'slug': str(self.id)})

    @property
    def get_actual_category(self):
        if self.sub_sub_category:
            return self.sub_sub_category
        if self.sub_category:
            return self.sub_category
        if self.category:
            return self.category
        return None

    def get_link_to_sub_category(self):
        if self.sub_category:
            return '<a href="%s">%s</a>' % (self.sub_category.get_absolute_url, self.sub_category)
        else:
            return ''


    def get_link_to_sub_sub_category(self):
        if self.sub_sub_category:
            return '<a href="%s">%s</a>' % (self.sub_sub_category.get_absolute_url, self.sub_sub_category)
        else:
            return ''


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

    def thumbnail_big(self):
        try:
            thumbnail_url = get_backend().get_thumbnail_url(
                self.photo,
                {
                    'size': (250, 250),
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


class Offer(models.Model):
    status = (
        ('new', _('Новое')),
        ('active', _('Активное')),
        ('inactive', _('Неактивное')),
        ('closed', _('Закрытое')),
    )

    user = models.ForeignKey(User, verbose_name=_(u'Автор'))
    message = models.TextField(verbose_name=_(u'Сообщение'))
    url = models.CharField(verbose_name=_(u'Ссылка на сайт'), max_length=250, null=True, blank=True)
    image = models.ImageField(verbose_name=_(u'Изображение'), upload_to='offer_images/', null=True, blank=True)
    file = models.FileField(verbose_name=_(u'Аттачмент'), upload_to='offer_files/', null=True, blank=True)
    price = models.DecimalField(verbose_name=_(u'Цена'), max_digits=19, decimal_places=2)
    status = models.CharField(verbose_name=_(u'Статус'), max_length=10, choices=status, default='message')
    created_at = models.DateTimeField(verbose_name=_(u'Когда создано?'), auto_now_add=True)

    def __unicode__(self):
        return '#%s: %s' % (self.id, self.message)


class OfferMessage(models.Model):
    offer = models.ForeignKey(Offer, verbose_name=_(u'Предложение'))
    new_price = models.DecimalField(verbose_name=_(u'Новая цена'), max_digits=19, decimal_places=2)
    message = models.TextField(verbose_name=_(u'Сообщение'))
    file = models.FileField(verbose_name=_(u'Аттачмент'), upload_to='offer_files/', null=True, blank=True)
    user = models.ForeignKey(User, verbose_name=_(u'Автор'), null=True, blank=True)

    def __unicode__(self):
        return self.message