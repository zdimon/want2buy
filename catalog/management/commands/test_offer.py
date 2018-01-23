from django.core.management.base import BaseCommand, CommandError
from catalog.models import City, Region
from bs4 import BeautifulSoup
import os
from django.core.cache import cache

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from catalog.form import save_offer


class Command(BaseCommand):
    def handle(self, *args, **option):
        print "Test offer"
        data = {'username': 'mmmmm', 'url': 'mmmm', 'price': '23', 'phone': '65756', 'file': None, 'announcement_id': '2454', 'email': 'mmmm@mmm.mm', 'desc': 'mmmmmm', 'user_id': 11}
        save_offer(data)
       
