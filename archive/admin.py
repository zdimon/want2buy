# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import *


def approve(modeladmin, request, queryset):
    for i in queryset:
        t = NewAnnouncement.objects.filter(id=i.id).values()[0]
        del t['id']
        Announcement.objects.create(**t)
        NewAnnouncement.objects.filter(id=i.id).delete()


def disapprove(modeladmin, request, queryset):
    for i in queryset:
        t = Announcement.objects.filter(id=i.id).values()[0]
        del t['id']
        NewAnnouncement.objects.create(**t)
        Announcement.objects.filter(id=i.id).delete()


class NewAnnouncementAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('thumbnail', 'title', 'category', 'sub_category', 'sub_sub_category')
    actions = [approve]


admin.site.register(NewAnnouncement, NewAnnouncementAdmin)


class AnnouncementAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('thumbnail', 'title', 'category', 'sub_category', 'sub_sub_category')
    actions = [disapprove]


admin.site.register(Announcement, AnnouncementAdmin)
