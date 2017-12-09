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

class SubSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'parent_sub_category')
    list_filter = ('parent_sub_category',)
admin.site.register(SubSubCategory, SubSubCategoryAdmin)


class RegionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Region, RegionAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    list_filter = ('region',)
admin.site.register(City, CityAdmin)
