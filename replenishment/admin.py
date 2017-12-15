# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Replanishment

from django.contrib import admin

# Register your models here.
class ReplanishmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')


admin.site.register(Replanishment, ReplanishmentAdmin)