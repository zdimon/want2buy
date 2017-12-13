# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from catalog.models import *
from archive.models import Announcement
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def catalog_main(request,slug):
    current = Category.objects.get(name_slug=slug)
    items = Announcement.objects.filter(category=current)
    paginator = Paginator(items, 20)
    page = request.GET.get('page',1)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    ctx = {
        'current': current,
        'items': items
    }
    return render(request, 'catalog/catalog.html', ctx)

def catalog_sub(request,slug):
    current = SubCategory.objects.get(name_slug=slug)
    items = Announcement.objects.filter(sub_category=current)
    paginator = Paginator(items, 20)
    page = request.GET.get('page',1)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    ctx = {
        'current': current,
        'items': items
    }    
    return render(request, 'catalog/sub_catalog.html', ctx)    

def catalog_sub_sub(request,slug):
    current = SubSubCategory.objects.get(name_slug=slug)
    items = Announcement.objects.filter(sub_sub_category=current)
    paginator = Paginator(items, 20)
    page = request.GET.get('page',1)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    ctx = {
        'current': current,
        'items': items
    }    
    return render(request, 'catalog/sub_sub_catalog.html', ctx)    