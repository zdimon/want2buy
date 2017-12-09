# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from main.models import Page


# Create your views here.

def home(request):
    page = Page.objects.get(alias='alias1')
    return render(request, 'home.html', {'page_in_template': page})

class PageObj():
    title = 'пустой'
    content = '---'

def page(request,alias='main'):
    try:
        page_obj = Page.objects.get(alias=alias)
    except:
        page_obj = PageObj()

    return render(request, 'home.html', {'page_in_template': page_obj})

def about(request):
    return render(request, 'about.html')