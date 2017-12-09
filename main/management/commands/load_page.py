# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from main.models import Page


class Command(BaseCommand):

    def handle(self, *args, **options):
        print 'Start'
        Page.objects.all().delete()
        
        p = Page()
        p.title = 'логин admin пароль 123'
        p.content = 'Conteentttt ttttt t tt '
        p.alias = 'main'
        p.meta_keywords = 'main'
        p.meta_description = 'main'
        p.meta_title = 'main'
        p.save()
        print 'Page main was created'