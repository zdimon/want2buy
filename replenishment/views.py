# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def replenishment_page(request):
    return render(request, 'replenishment/replenishment.html')
