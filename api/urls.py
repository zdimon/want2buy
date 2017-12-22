# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from .views.offer import *
from .views.announcement import *
from .views.region import *
from .views.categories import *

router = routers.DefaultRouter()
router.register(r'new_announcement', NewAnnouncementViewSet)
router.register(r'announcement', AnnouncementViewSet)
router.register(r'offer', OfferListViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^regions$', regions),
    url(r'categories$', categories),
    url(r'announcement/detail/(?P<id>[0-9]+)$', announcement_detail),
    url(r'offer/detail/(?P<id>[0-9]+)$', offer_detail),
    url(r'offer/(?P<id>[0-9]+)/set/current/$', set_current_offer),
    url(r'offer/save/message/$', offer_save_message),

    
]
