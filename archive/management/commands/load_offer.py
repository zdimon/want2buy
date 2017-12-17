# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from catalog.models import *
from account.models import Profile
from want2buy.settings import BASE_DIR
import json
from django.core.files import File
import shutil
from archive.models import NewAnnouncement, Announcement, Offer, OfferMessage
from catalog.models import *

 

class Command(BaseCommand):

    def handle(self, *args, **options):
        print 'Clearing the table'
        OfferMessage.objects.all().delete()
        Offer.objects.all().delete()
        print 'Start loading..'
        cnt = 0
        for a in Announcement.objects.all().order_by('-id'):
            cnt = cnt + 1
            if cnt == 10:
                break
            print 'Process announcement...%s' % a.id
            for u in User.objects.exclude(id=a.user_id):
                print 'Saving .....'
                o = Offer()
                o.user = u
                o.message = 'test message'
                o.url = 'test url'
                o.price = 10
                o.announcement = a
                o.save()

                m = OfferMessage()
                m.offer = o
                m.new_price = 20
                m.message = 'I have a new dial'
                m.user = u
                m.save()

                m = OfferMessage()
                m.offer = o
                m.new_price = 20
                m.message = 'I have a new dial 2'
                m.user = u
                m.save()

            #print a.user
            #break
           