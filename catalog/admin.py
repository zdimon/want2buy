# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from catalog.models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')
    list_filter = ('parent_category',)
admin.site.register(SubCategory, SubCategoryAdmin)
