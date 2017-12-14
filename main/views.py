# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from main.models import Page
from catalog.models import Category
from archive.models import Announcement
from django.views.decorators.csrf import csrf_exempt
from jsonview.decorators import json_view

@csrf_exempt
@json_view
def update(request):
    import subprocess
    command = 'git pull'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = []
    for line in p.stdout.readlines():
        print line
        out.append(line)
    retval = p.wait()
    command = 'tsc'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line
        out.append(line)   
    retval = p.wait() 
    return {'status': 'ok', 'message': out}


def home(request):
    page = Page.objects.get(alias='main')
    categories = Category.objects.all()[0:12]
    announcements = Announcement.objects.all().order_by('?')[0:6]
    #import pdb; pdb.set_trace()
    return render(request, 'home.html', {
        'page_in_template': page, 
        'categories': categories,
        'announcements': announcements
        })

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