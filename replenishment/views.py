# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from replenishment.froms import ReplanishmentForm
from django.shortcuts import render_to_response, redirect
from replenishment.models import Replanishment

from django.shortcuts import render

# Create your views here.


def replenishment_page(request):
    args = {}
    if request.method == 'POST':
        form = ReplanishmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print form.errors
    else:
        args['form'] = ReplanishmentForm()

    return render(request, 'replenishment/replenishment.html', args)
