# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0012_auto_20171217_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='offermessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2018-01-01', verbose_name='\u041a\u043e\u0433\u0434\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u043e?'),
            preserve_default=False,
        ),
    ]
