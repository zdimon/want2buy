# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.contrib.auth import authenticate, login
from catalog.models import *
from image_cropping import ImageRatioField
from image_cropping import ImageCropField
from image_cropping.utils import get_backend


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name=_(u'Пользователь'))
    first_name = models.CharField(max_length=50, blank=True, verbose_name=_(u'Имя'))
    last_name = models.CharField(max_length=50, blank=True, verbose_name=_(u'Фамилия'))
    middle_name = models.CharField(max_length=50, blank=True, verbose_name=_(u'Отчество'))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_(u'дата регистрации'))
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name=_(u'Аватарка'))
    phone = models.CharField(max_length=50, blank=True, verbose_name=_(u'Номер телефона'))
    site = models.URLField(max_length=50, blank=True, verbose_name=_(u'Сайт'))
    address = models.CharField( max_length=150, blank=True, verbose_name=_(u'Адрес'))
    rating = models.IntegerField(default=0, null=True, blank=True, verbose_name=_(u'Рейтинг'))
    region = models.ForeignKey(Region, null=True, blank=True, verbose_name=_(u'Регион'))
    city = models.ForeignKey(City, null=True, blank=True, verbose_name=_(u'Город'))
    account = models.DecimalField(default=0, max_digits=5, decimal_places=2, null=True, blank=True,
                                  verbose_name=_(u'Счет'))
    cropping = ImageRatioField('avatar', '100x100', verbose_name=_(u'Кадрирование'))

    def __unicode__(self):
        return self.user.username

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.middle_name)

    def get_thumbnail_url(self):
        try:
            thumbnail_url = get_backend().get_thumbnail_url(
                self.avatar,
                {
                    'size': (100, 100),
                    'box': self.cropping,
                    'crop': True,
                    'detail': True,
                }   
            )
            return thumbnail_url
        except:
            return "/static/images/noimage.png"   

    def thumbnail(self):
        return '<img class="img-responsive" src="%s"  />' % self.get_thumbnail_url()
        

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)


class Testimonial(models.Model):
    author = models.ForeignKey(Profile, verbose_name=_(u'Пользователь'))
    content = models.TextField(verbose_name=_(u'Содержание'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_(u'Дата создания'))


class Transaction(models.Model):
    user = models.ForeignKey(Profile, verbose_name=_(u'Пользователь'))
    ammount = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name=_(u'Количество'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_(u'Дата создания'))
