from django.core.management.base import BaseCommand, CommandError
from catalog.models import Category, SubCategory, SubSubCategory
import json
from django.core.cache import cache
from want2buy.settings import BASE_DIR
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        print 'Start loading categories'
        Category.objects.all().delete()
        SubCategory.objects.all().delete()
        categories = json.load(open(os.path.join(BASE_DIR, 'data', 'categories.json')))['result']
        for i in categories:
            c = Category(name=i['name'])
            c.save()
            for j in i['sub_cat']:
                s = SubCategory(name=j['name'], parent_category=c)
                s.save()
                for h in j['sub']:
                    _s = SubSubCategory(name=h, parent_sub_category=s)
                    _s.save()
                print 'Process ... %s' % s.name
        cache.delete('categories')
