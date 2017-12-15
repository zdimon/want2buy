from django.core.management.base import BaseCommand, CommandError
from catalog.models import City, Region, Category
from bs4 import BeautifulSoup
import os
from django.core.cache import cache
from want2buy.settings import BASE_DIR
import json
from django.core.files import File
import shutil



class Command(BaseCommand):
    def handle(self, *args, **option):
        path = '%s/data/images/catalog/' % BASE_DIR
        try:
            shutil.rmtree('%s/media/catalog_main' % path)
        except:
            pass
        print "Start loading pictures from %s" % path
        for c in Category.objects.all():
            print 'Process ...%s' % c.name_slug
            image_name = '%s.jpg' % c.name_slug
            image_path = path+image_name
            try:
                c.photo.save(
                    image_name,
                    File(open(image_path))
                    )
                print 'Success.....'
            #break
            except:
                print 'errror!'
