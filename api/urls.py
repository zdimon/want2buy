# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^regions$', regions),
    url(r'categories$', categories),
    url(r'announcement/(?P<slug>[0-9]+)', announcement)
]
