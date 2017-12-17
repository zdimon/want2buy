# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^register/$', MyRegistrationView.as_view(), name='register'),
    url(r'^profile/edit$', ProfileEditView.as_view(), name='profile_edit'),
    url(r'^registration/done', registration_done, name='registration_done'),
    url(r'^activation/done', activation_done, name='activation_done'),
    url(r'^activate/(?P<activation_key>[-:\w]+)/$', MyActivationView.as_view(),name='registration_activate'),
    url(r'^', dashboard, name='dashboard'),
]