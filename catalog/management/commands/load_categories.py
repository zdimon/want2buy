from django.core.management.base import BaseCommand, CommandError
from catalog.models import Category, SubCategory, SubSubCategory
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
                s = SubCategory(name=j['name'], parent_category=c)
                s.save()
                for h in j['sub']:
                    _s = SubSubCategory(name=h, parent_sub_category=s)
                    _s.save()
                print 'Process ... %s' % s.name