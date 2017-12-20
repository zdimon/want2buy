# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jsonview.decorators import json_view
from django.core.cache import cache
from archive.models import Offer, OfferMessage
from django.core import serializers
import json
from rest_framework import viewsets
from api.serializers import OfferSerializer

@json_view
def offer_detail(request):
    out = {}
    return out
    
class OfferListViewSet(viewsets.ModelViewSet):
    serializer_class =OfferSerializer
    queryset = Offer.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Offer.objects.filter(user=user)