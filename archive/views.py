# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import NewAnnouncementForm
from .models import NewAnnouncement
from django.http import HttpResponseRedirect
# Create your views here.

def add_announce(request):
    
    if request.method == 'POST':
        form = NewAnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_announcement/done')
    else:
        a = NewAnnouncement()
        a.user = request.user
        form = NewAnnouncementForm(instance=a)

    return render(request, 'archive/add_announce.html',{'form': form})
