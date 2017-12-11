# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from catalog.models import *
from account.models import Profile
from want2buy.settings import BASE_DIR
import json
from django.core.files import File
import shutil
from archive.models import NewAnnouncement

def get_user(name):
    return User.objects.get(username=name)

def get_city(city):
    return City.objects.get(name=city)

def get_catalog(name):
    return SubSubCategory.objects.get(name=name)    

class Command(BaseCommand):

    def handle(self, *args, **options):
        path = '%s/data/new_announcements.json' % BASE_DIR
        try:
            shutil.rmtree('%s/media/new_announcements' % BASE_DIR)
        except:
            pass
        print 'Clearing the table'
        NewAnnouncement.objects.all().delete()
        print 'Start loading users from %s' % path
        f = open(path)
        cnt = f.read()
        f.close()
        js = json.loads(cnt)
        for i in js:
            print 'Creating a new record....%s' % i['title']
            n = NewAnnouncement()
            n.title = i['title']
            n.user = get_user(i['user'])
            n.category = get_catalog(i['category']).parent_sub_category.parent_category
            n.sub_category = get_catalog(i['category']).parent_sub_category
            n.sub_sub_category = get_catalog(i['category'])
            n.city = get_city(i['city'])
            n.new_bu = i['new_bu']
            n.opt_roznica = i['opt_roznica']
            n.info = i['info']
            n.price = i['price']
            n.ammount = i['ammount']
            n.save()
            image_path = '%s/data/images/%s' % (BASE_DIR, i['photo'])
            n.photo.save(
                i['photo'],
                File(open(image_path))
                )   