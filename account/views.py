# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def forget_password(request):
    message = None
    if request.method == 'POST':
        print request.POST['username']
    else:
        pass

    return render(request, 'account/forget_password.html', {'message': message})    