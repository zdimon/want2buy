# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jsonview.decorators import json_view
from django.core.cache import cache
from catalog.models import Region, City
from django.core import serializers


@json_view
def regions(request):
    if not cache.get('regions'):
        out = []
        for r in Region.objects.all():
            reg = {'id': r.id, 'name': r.name, 'cities': []}
            for c in City.objects.filter(region=r):
                reg['cities'].append({'id': c.id, 'name': c.name, 'lat': c.lat, 'lon': c.lon})
            out.append(reg)
            cache.set('regions', out, 60 * 60 * 24)
    else:
        out = cache.get('regions')
    return out

