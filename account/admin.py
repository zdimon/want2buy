# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import *

class ProfileAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)

# Register your models here.
