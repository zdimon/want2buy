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

    user = models.ForeignKey(User, verbose_name=_(u'Пользователь'))
    title = models.CharField(max_length=250, verbose_name=_(u'Заголовок'))
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name=_(u'Категория'))
    sub_category = models.ForeignKey(SubCategory, null=True, blank=True, verbose_name=_(u'Подкатегория'))
    sub_sub_category = models.ForeignKey(SubSubCategory, null=True, blank=True, verbose_name=_(u'Под подкатегория'))
    new_category = models.CharField(max_length=250, null=True, blank=True, verbose_name=_(u'Новая категория'))
    new_bu = models.CharField(max_length=10, choices=new, default='new', verbose_name=_(u'Новое/БУ'))
    opt_roznica = models.CharField(max_length=10, choices=opt, default='retail', verbose_name=_(u'Опт/Розница'))
    type = models.CharField(max_length=10, choices=tp, default='good', verbose_name=_(u'Тип'))
    once = models.CharField(max_length=10, choices=once, default='once', verbose_name=_(u'Одноразовая/Постоянно'))
    price = models.DecimalField(verbose_name=_(u'Цена'), max_digits=19, decimal_places=2)
    ammount = models.IntegerField(default=1, verbose_name=_(u'Количество'))
    city = models.ForeignKey(City, null=True, blank=True, verbose_name=_(u'Город'))
    region = models.ForeignKey(Region, null=True, blank=True, verbose_name=_(u'Регион'))
    new_city = models.CharField(max_length=250, null=True, blank=True, verbose_name=_(u'Новый город'))
    info = models.TextField(null=True, blank=True, verbose_name=_(u'Информация'))
    photo = models.ImageField(upload_to='announcements/', null=True, blank=True, verbose_name=_(u'Фото'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_(u'дата создания'))
    cropping = ImageRatioField('photo', '150x150', verbose_name=_(u'Кадрирование'))
    is_paid = models.BooleanField(default=False, verbose_name=_(u'Оплачиваемое'))
    date_expire = models.DateField(null=True, blank=True, verbose_name=_(u'Дата окончания'))
    date_paid_expire = models.DateField(null=True, blank=True, verbose_name=_(u'Дата окончания оплаты'))
    current_offer = models.IntegerField(null=True, blank=True, verbose_name=_(u'Текущее предложение'))
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

    @property
    def get_link_to_sub_category(self):
        if self.sub_category:
            return '<a href="%s">%s</a>' % (self.sub_category.get_absolute_url, self.sub_category)
        else:
            return ''

    @property
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


    def get_photo_url(self):
        try:
            return self.photo.url
        except:
            return '/static/images/noimage.png'    

    def get_thumbnail_url(self):
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
            return thumbnail_url
        except:
            return '/static/images/noimage.png'    

    def thumbnail(self):
        return '<img class="img-responsive" src="%s"  />' % self.get_thumbnail_url()
       
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

#Offer.objects.raw('delete * from archive_offer')

class Offer(models.Model):
    status = (
        ('new', _('Новое')),
        ('active', _('Активное')),
        ('inactive', _('Неактивное')),
        ('waiting', _('Ожидает подтверждения')),
        ('closed', _('Закрытое')),
    )

    seller = models.ForeignKey(User, related_name='seller', verbose_name=_(u'Продавец'), null=True, blank=True)
    buyer = models.ForeignKey(User, related_name='buyer', verbose_name=_(u'Покупатель'), null=True, blank=True)
    announcement = models.ForeignKey(Announcement, verbose_name=_(u'Объявление'))
    message = models.TextField(verbose_name=_(u'Сообщение'))
    url = models.CharField(verbose_name=_(u'Ссылка на сайт'), max_length=250, null=True, blank=True)
    image = models.ImageField(verbose_name=_(u'Изображение'), upload_to='offer_images/', null=True, blank=True)
    file = models.FileField(verbose_name=_(u'Аттачмент'), upload_to='offer_files/', null=True, blank=True)
    price = models.DecimalField(verbose_name=_(u'Цена'), max_digits=19, decimal_places=2)
    status = models.CharField(verbose_name=_(u'Статус'), max_length=10, choices=status, default='new')
    created_at = models.DateTimeField(verbose_name=_(u'Когда создано?'), auto_now_add=True)
    is_current = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    def __unicode__(self):
        return '#%s: %s' % (self.id, self.message)

    def getIcon(self):
        return '/static/images/icons/%s.png' % self.status



class OfferMessage(models.Model):
    offer = models.ForeignKey(Offer, verbose_name=_(u'Предложение'))
    new_price = models.DecimalField(verbose_name=_(u'Новая цена'), max_digits=19, decimal_places=2, null=True, blank=True)
    message = models.TextField(verbose_name=_(u'Сообщение'))
    file = models.FileField(verbose_name=_(u'Аттачмент'), upload_to='offer_files/', null=True, blank=True)
    user = models.ForeignKey(User, verbose_name=_(u'Автор'), null=True, blank=True)
    created_at = models.DateTimeField(verbose_name=_(u'Когда создано?'), auto_now_add=True)
    def __unicode__(self):
        return self.message
