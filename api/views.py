# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jsonview.decorators import json_view
from django.core.cache import cache
from catalog.models import Region, City, Category, SubCategory, SubSubCategory
from archive.models import Announcement
from django.core import serializers
import json
@json_view
def regions(request):
    if not cache.get('regions'):
        out = []
        for r in Region.objects.all():
            reg = {'id': r.id, 'name': r.name, 'cities': []}
            for c in City.objects.filter(region=r):
                reg['cities'].append({'id': c.id, 'name': c.name, 'lat': c.lat, 'lon': c.lon})
            out.append(reg)
            cache.set('regions', out, 60*60*24)
    else:
        out = cache.get('regions')
    return out


@json_view
def categories(request):
    if not cache.get('categories'):
        out = []
        for c in Category.objects.all():
            cat = {'id': c.id, 'name': c.name, 'sub_category': []}
            for s in SubCategory.objects.filter(parent_category=c):
                sub = {'id': s.id, 'name': s.name, 'category_id': s.parent_category.id,  'sub_category': []}
                for ss in SubSubCategory.objects.filter(parent_sub_category=s):
                    sub['sub_category'].append({'id': ss.id, 'name': ss.name})
                cat['sub_category'].append(sub)
            out.append(cat)
        cache.set('categories', out, 60*60*24)
    else:
        out = cache.get('categories')
    return out


@json_view
def announcement(request, slug):
    if len(Announcement.objects.filter(id=slug)) != 0:
        tmp = json.loads(serializers.serialize('json', Announcement.objects.filter(id=slug)))[0]['fields']
        out = {'user_id': tmp['user'], 'title': tmp['title'], 'category': Category.objects.get(id=tmp['category']).name,
               'sub_category': SubCategory.objects.get(id=tmp['sub_category']).name,
               'sub_sub_category': SubSubCategory.objects.get(id=tmp['sub_sub_category']).name,
               'new_category': tmp['new_category'], 'new_bu': tmp['new_bu'], 'opt_roznica': tmp['opt_roznica'],
               'type': tmp['type'], 'once': tmp['once'], 'price': tmp['price'], 'amount': tmp['ammount'],
               'city': City.objects.get(id=tmp['city']).name, 'photo': Announcement.objects.get(id=slug).photo.url,
               'created_at': tmp['created_at'], 'is_paid': tmp['is_paid'], 'expire': tmp['date_expire'], 'paid_expire': tmp['date_paid_expire']}
    else:
        out = {'message': 'No such element'}
    return out
