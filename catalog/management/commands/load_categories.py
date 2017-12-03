from django.core.management.base import BaseCommand, CommandError
from catalog.models import Category, SubCategory
import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):
    @staticmethod
    def parse():
        r = requests.get('https://www.olx.ua/')
        soup = BeautifulSoup(r.text, 'html.parser')
        a = soup.findAll("div", {"class": "maincategories"})
        items_raw = a[0].findAll("div", {"class": "item"})
        items = []
        for i in items_raw:
            _id = i.a['data-id']
            tmp = a[0].find("div", {"data-subcategory": _id}).findAll("span", {"class": "block link category-name"})
            sub_cat = []
            for j in tmp:
                sub_cat.append(j.span.string)
            items.append({"name": i.span.string, "sub_cat": sub_cat})
        return items

    def handle(self, *args, **options):
        print 'Start loading categories'
        Category.objects.all().delete()
        SubCategory.objects.all().delete()
        categories = self.parse()
        for i in categories:
            c = Category(name=i['name'])
            c.save()
            for j in i['sub_cat']:
                s = SubCategory(name=j, parent_category=c)
                s.save()
                print 'Process ... %s' % s.name