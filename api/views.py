# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jsonview.decorators import json_view
from django.core.cache import cache
from catalog.models import Region, City, Category, SubCategory, SubSubCategory
from archive.models import Announcement, NewAnnouncement, Offer
from django.core import serializers
import json
from rest_framework import viewsets
from .serializers import NewAnnoncementSerializer, AnnoncementSerializer


@json_view
def regions(request):
    if not cache.get('regions'):
        out = []
        for r in Region.objects.all():
            reg = {'id': r.id, 'name': r.name, 'cities': []}
            for c in City.objects.filter(region=r):
                reg['cities'].append({'id': c.id, 'name': c.name, 'lat': c.lat, 'lon': c.lon})
            out.append(reg)
            cache.set('regions', out, 60 * 60 * 24)
    else:
        out = cache.get('regions')
    return out


@json_view
def categories(request):
    if not cache.get('categories'):
        out = []
        for c in Category.objects.all():
            cat = {'id': c.id, 'name': c.name, 'sub_category': []}
            for s in SubCategory.objects.filter(parent_category=c):
                sub = {'id': s.id, 'name': s.name, 'category_id': s.parent_category.id, 'sub_category': []}
                for ss in SubSubCategory.objects.filter(parent_sub_category=s):
                    sub['sub_category'].append({'id': ss.id, 'name': ss.name})
                cat['sub_category'].append(sub)
            out.append(cat)
        cache.set('categories', out, 60 * 60 * 24)
    else:
        out = cache.get('categories')
    return out

@json_view
def announcement_detail(request, id):

    if len(Announcement.objects.filter(id=id)) != 0:
        a = Announcement.objects.filter(id=id)[0]
        try:
            subsub = a.sub_sub_category.name
        except AttributeError:
            subsub = None
        try:
            sub = a.sub_category.name
        except AttributeError:
            sub = None
        out = {
               'current_user': {
                   'name': request.user.profile.full_name
               }, 
               'id': a.id,
               'thumbnail': a.get_thumbnail_url(),
               'user_id': a.user_id,
               'cnt_offers': a.offer_set.all().count(), 
               'title': a.title, 
               'category': a.category.name,
               'sub_category': sub,
               'sub_sub_category': subsub,
               'new_category': a.new_category, 'new_bu': a.get_new_bu_display(), 'opt_roznica': a.get_opt_roznica_display(),
               'type': a.type, 'once': a.once, 'price': a.price, 'amount': a.ammount,
               'city': a.city.name, 'photo': a.photo.url,
               'created_at': a.created_at.strftime('%d %b %Y %H:%M'), 'is_paid': a.is_paid, 'expire': a.date_expire,
               'paid_expire': a.date_paid_expire, 'offers': []}
        offers = Offer.objects.filter(announcement_id=id)
        _offers = []
        if len(offers) != 0:
            for i in offers:
                try:
                    image = i.image.url
                except ValueError:
                    image = None
                try:
                    file = i.file.url
                except ValueError:
                    file = None
                user = i.user.profile
                user_obj = {
                    'name': user.full_name,
                    'id': user.user_id,
                    'thumbnail': user.get_thumbnail_url(),
                    'rating': user.rating
                }
                messages = i.offermessage_set.all()
                mesobj = []
                for m in messages:
                    muser_obj = {
                        'name': m.user.profile.full_name,
                        'id': m.user.profile.user_id,
                        'thumbnail': m.user.profile.get_thumbnail_url(),
                        'rating': m.user.profile.rating
                    }
                    mesobj.append({
                        'user': muser_obj,
                        'message': m.message,
                        'new_price': m.new_price,
                        'created_at': m.created_at.strftime('%d %b %Y %H:%M')
                    })
                _offers.append({'user': user_obj,
                                'id': i.id,
                                'message': i.message,
                                'messages': mesobj,
                                'cnt_messages': i.offermessage_set.all().count(),
                                'url': i.url,
                                'image': image,
                                'file': file,
                                'price': i.price,
                                'status': i.status,
                                'created_at': i.created_at.strftime('%d %b %Y %H:%M')})
        out.update({'offers': _offers})
    else:
        out = {'message': 'No such element'}
    return out


class NewAnnouncementViewSet(viewsets.ModelViewSet):
    queryset = NewAnnouncement.objects.all()
    serializer_class = NewAnnoncementSerializer

    def get_queryset(self):
        user = self.request.user
        return NewAnnouncement.objects.filter(user=user)


class AnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class = AnnoncementSerializer
    queryset = Announcement.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Announcement.objects.filter(user=user)
