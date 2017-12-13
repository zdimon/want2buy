from django.core.management.base import BaseCommand, CommandError
from catalog.models import Category, SubCategory, SubSubCategory
import requests
from bs4 import BeautifulSoup
from want2buy.settings import BASE_DIR
import os
import json

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
            tmp = a[0].find("div", {"data-subcategory": _id}).findAll("li", {'class', 'fleft'})
            sub_cat = []
            for j in tmp:
                sub_sub_cat = []
                name = j.find('span', {'class', 'block link category-name'}).span.text
                url = j.a['href']
                _r = requests.get(url)
                _soup = BeautifulSoup(_r.text, 'html.parser')
                _sub_cat = _soup.find('div', {'id': 'topLink'})
                if _sub_cat is not None:
                    span = _sub_cat.findAll('span', {'class': 'link'})
                    for h in span:
                        if h.span.text not in sub_sub_cat:
                            sub_sub_cat.append(h.span.text)
                sub_cat.append({"name": name, "sub": sub_sub_cat})
            items.append({"name": i.span.string, "sub_cat": sub_cat})
        return {'result': items}

    def handle(self, *args, **options):
        print 'Start loading categories'
        a = self.parse()
        open(os.path.join(BASE_DIR, 'data', 'categories.json'), 'w').write(json.dumps(a, sort_keys=True))
