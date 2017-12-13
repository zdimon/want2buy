# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from main.models import Page
from catalog.models import Category


# Create your views here.

def update(request):
    return render(request, 'home.html')


def home(request):
    page = Page.objects.get(alias='main')
    categories = Category.objects.all()[0:12]
    #import pdb; pdb.set_trace()
    return render(request, 'home.html', {'page_in_template': page, 'categories': categories})

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