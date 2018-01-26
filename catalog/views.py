# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from catalog.models import *
from archive.models import Announcement
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import *
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

# Create your views here.

def catalog_main(request,slug):
    current = Category.objects.get(name_slug=slug)
    items = Announcement.objects.filter(category=current).order_by('-id')
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
    items = Announcement.objects.filter(sub_category=current).order_by('-id')
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
    items = Announcement.objects.filter(sub_sub_category=current).order_by('-id')
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

def annoncement_detail(request,slug):
    item = Announcement.objects.get(pk=slug)

    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            form = OfferForm(initial={'announcement_id': item.id })
            messages.success(request, _('Ваше предложение отправлено покупателю.'))
    else:
        if request.user.is_authenticated():
            form = OfferForm(initial={
                'username': request.user.profile.first_name,
                'email': request.user.username,
                'phone': request.user.profile.phone,
                'announcement_id': item.id
                })
        else:
            form = OfferForm(initial={'announcement_id': item.id })

    
    ctx = {
        'item': item,
        'form': form
    }    
    return render(request, 'catalog/annoncement_detail.html', ctx)    