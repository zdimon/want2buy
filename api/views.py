# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from jsonview.decorators import json_view
from catalog.models import Region, City

@json_view
def regions(request):
    out = []
    for r in Region.objects.all():
        reg = {'id': r.id, 'name':  r.name, 'cities': []}
        for c in City.objects.filter(region=r):
            reg['cities'].append({'id': c.id, 'name': c.name})
        out.append(reg)
    return out
