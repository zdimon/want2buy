# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import NewAnnouncementForm
from .models import NewAnnouncement
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
# Create your views here.

def add_announce(request):
    
    if request.method == 'POST':
        form = NewAnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _('Объявление было сохранено. После модерации оно появиться на сайте.'))
            return redirect('/dashboard/index')
    else:
        a = NewAnnouncement()
        a.user = request.user
        form = NewAnnouncementForm(instance=a)

    return render(request, 'archive/add_announce.html',{'form': form})
