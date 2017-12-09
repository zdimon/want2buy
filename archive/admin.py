# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import *

class NewAnnouncementAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('thumbnail', 'title', 'full_category')
admin.site.register(NewAnnouncement, NewAnnouncementAdmin)
