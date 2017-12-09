# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from main.models import Page


class Command(BaseCommand):

    def handle(self, *args, **options):
        print 'Start'
        Page.objects.all().delete()
        for i in range(1, 10):
            p = Page()
            p.title = 'логин admin пароль 123'
            p.content = 'Conteentttt ttttt t tt '
            p.alias = 'alias%s' % i
            p.meta_keywords = 'alias%s' % i
            p.meta_description = 'alias%s' % i
            p.meta_title = 'meta_title %s' % i
            p.save()
            print 'Page %s was created' % i