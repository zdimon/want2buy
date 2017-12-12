# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from jsonview.decorators import json_view
from django.core.cache import cache
from catalog.models import Region, City, Category, SubCategory, SubSubCategory


@json_view
def regions(request):
    out = []
    for r in Region.objects.all():
        reg = {'id': r.id, 'name': r.name, 'cities': []}
        for c in City.objects.filter(region=r):
            reg['cities'].append({'id': c.id, 'name': c.name})
        out.append(reg)
    return out


@json_view
def categories(request):
    if not cache.get('categories'):
        out = []
        for c in Category.objects.all():
            cat = {'id': c.id, 'name': c.name, 'sub_category': []}
            for s in SubCategory.objects.filter(parent_category=c):
                sub = {'id': s.id, 'name': s.name, 'sub_category': []}
                for ss in SubSubCategory.objects.filter(parent_sub_category=s):
                    sub['sub_category'].append({'id': ss.id, 'name': ss.name})
                cat['sub_category'].append(sub)
            out.append(cat)
        cache.set('categories', out, 60*60*24)
    else:
        out = cache.get('categories')
    return out
