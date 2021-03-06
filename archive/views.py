# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import NewAnnouncementForm
from .models import NewAnnouncement
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_announce(request):
    
    if request.method == 'POST':
        form = NewAnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.save()
            a.approve()
            messages.success(request, _('Объявление было сохранено. После модерации оно появиться на сайте.'))
            return redirect('/dashboard/index')
    else:
        a = NewAnnouncement()
        a.user = request.user
        form = NewAnnouncementForm(instance=a)

    return render(request, 'archive/add_announce.html',{'form': form})
