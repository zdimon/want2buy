# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'alias')


admin.site.register(Page, PageAdmin)


class PageFeedback(admin.ModelAdmin):
    list_display = ('subject', 'resolved')


admin.site.register(Feedback, PageFeedback)
