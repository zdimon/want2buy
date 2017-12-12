from django.core.management.base import BaseCommand, CommandError
from catalog.models import City, Region
from bs4 import BeautifulSoup
import os
from django.core.cache import cache

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse():
    _file = open(os.path.join(BASE_DIR, '../../data/ukraine-regions.xml')).read()
    soup = BeautifulSoup(_file, 'html.parser')
    data = []
    for i in soup.findAll('region'):
        reg = i.attrs['name']
        tmp = []
        for j in i.findAll('city'):
            name = j.attrs['name']
            lon = j.attrs['lon']
            lat = j.attrs['lat']
            tmp.append({'name': name, 'lon': lon, 'lat': lat})
        data.append({'region': reg, 'city': tmp})
    return data


class Command(BaseCommand):
    def handle(self, *args, **option):
        print "Start loading cities"
        City.objects.all().delete()
        Region.objects.all().delete()
        a = parse()
        for i in a:
            r = Region(name=i['region'])
            r.save()
            for j in i['city']:
                c = City(region=r, name=j['name'], lat=j['lat'], lon=j['lon'])
                c.save()
                print 'Process ... %s' % c.name
        cache.delete('regions')
