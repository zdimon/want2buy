# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jsonview.decorators import json_view
from django.core.cache import cache
from archive.models import Offer, OfferMessage, Announcement
from django.core import serializers
import json
from rest_framework import viewsets
from api.serializers import OfferSerializer
from rest_framework.permissions import IsAuthenticated
from api.json_auth import json_auth
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
@json_auth
@json_view
def offer_save_message(request):
    obj = json.loads(request.body)
    print obj
    offer = Offer.objects.get(pk=obj['offer_id'])
    m = OfferMessage()
    m.offer = offer
    m.message = obj['message']
    m.user = offer.announcement.user
    try:
        m.new_price = int(obj['new_price'])
    except:
        pass
    m.save()
    return {'status': 0, 'message': 'Success'}

@json_auth
@json_view
def set_current_offer(request,id):
    offer = Offer.objects.get(pk=id)
    Offer.objects.filter(buyer=offer.buyer).update(is_current=False)
    offer.is_current = True
    offer.status = 'active'
    offer.save()
    return {'status': 0, 'message': 'Ok'}

@json_auth
@json_view
def set_current_offer_in_announcement(request,announcement_id, offer_id):
    an = Announcement.objects.get(pk=announcement_id)
    an.current_offer = offer_id
    an.save()
    offer = Offer.objects.get(pk=offer_id)
    offer.status = 'active'
    offer.save()    
    return {'status': 0, 'message': offer_id} 


@json_auth
@json_view
def offer_detail(request,id):
    offer = Offer.objects.get(pk=id)
    messages = []
    for m in offer.offermessage_set.all().order_by('id'):
        messages.append(
            {
                'id': m.id,
                'message': m.message,
                'user': {'name': m.user.profile.full_name,
                         'thumbnail': m.user.profile.get_thumbnail_url(),
                         'id': m.user.id
                        },
                'new_price': m.new_price,
                'created_at': m.created_at
            }
        )
    out = {
        'id': offer.id,
        'title': offer.announcement.title,
        'price': offer.price,
        'thumbnail': offer.announcement.get_thumbnail_url(),
        'message': offer.message,
        'created_at': offer.created_at,
        'messages': messages,
        'user': {'name': offer.buyer.profile.full_name,
                    'thumbnail': offer.buyer.profile.get_thumbnail_url(),
                    'id': offer.buyer.id
                }        
    }
    return out
    
class OfferListViewSet(viewsets.ModelViewSet):
    serializer_class =OfferSerializer
    queryset = Offer.objects.all()
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user = self.request.user
        return Offer.objects.filter(buyer=user).order_by('-is_current')


@json_auth
@json_view
def accept_offer(request,id):
    offer = Offer.objects.get(pk=id)
    return {'status': 0, 'message': 'OKEY'}