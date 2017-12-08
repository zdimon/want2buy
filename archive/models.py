# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



# Create your models here.


class NewAnnouncement(models.Model):
    new = (
        ('new', 'Новое'),
        ('used', 'БУ'),
    )

    opt = (
        ('opt', 'Опт'),
        ('retail', 'Розница'),
    )

    user_id = models.ForeignKey('account.Profile')
    title = models.TextField()
    category_id = models.ForeignKey('catalog.SubCategory')
    new_category = models.TextField()
    new_bu = models.CharField(max_length=10, choices=new)
    opt_roznica = models.CharField(max_length=10, choices=opt)
    price = models.FloatField()
    ammount = models.IntegerField()
    city_id = models.ForeignKey('catalog.City')
    info = models.TextField
    photo = models.ImageField()
    created_at = models.DateField()
