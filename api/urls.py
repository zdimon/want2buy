# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from .views import *
from rest_framework import routers
from .views import NewAnnouncementViewSet, AnnouncementViewSet

router = routers.DefaultRouter()
router.register(r'new_announcement', NewAnnouncementViewSet)
router.register(r'announcement', AnnouncementViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^regions$', regions),
    url(r'categories$', categories),
    url(r'announcement/detail/(?P<id>[0-9]+)$', announcement_detail)
]
