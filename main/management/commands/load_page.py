from django.core.management.base import BaseCommand, CommandError
from main.models import Page, Category, SubCategory
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
        print 'Start'
        Page.objects.all().delete()
        Category.objects.all().delete()
        SubCategory.objects.all().delete()
        categories = self.parse()
        for i in range(1, 10):
            p = Page()
            p.title = 'First page %s' % i
            p.content = 'Conteentttt ttttt t tt '
            p.alias = 'alias%s' % i
            p.meta_keywords = 'alias%s' % i
            p.meta_description = 'alias%s' % i
            p.meta_title = 'meta_title %s' % i
            p.save()
            print 'Page %s was created' % i

        for i in categories:
            c = Category(name=i['name'])
            c.save()
            for j in i['sub_cat']:
                s = SubCategory(name=j, parent_category=c, url="")
                s.save()