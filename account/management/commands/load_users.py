from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from account.models import Profile
from want2buy.settings import BASE_DIR
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        path = '%s/data/users.json' % BASE_DIR
        print 'Start loading users from %s' % path
        Profile.objects.all().delete()
        User.objects.all().delete()
        f = open(path)
        cnt = f.read()
        f.close()
        js = json.loads(cnt)
        for i in js:
            u = User()
            u.username = i['username']
            u.email = i['username']
            u.set_password(i['password'])
            u.is_active = True
            if i['is_admin'] == True:
                u.is_superuser = True
                u.is_staff = True
            u.save()
            p = u.profile    
            p.first_name = i['first_name']
            p.last_name = i['last_name']
            p.middle_name = i['middle_name']
            p.phone = i['phone']
            p.address = i['address']
            p.rating = i['rating']
            p.account = i['account']
            p.site = i['site']
            p.save()

            print i['username']
