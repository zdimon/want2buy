# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0020_auto_20171229_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.CharField(choices=[('new', '\u041d\u043e\u0432\u043e\u0435'), ('active', '\u0410\u043a\u0442\u0438\u0432\u043d\u043e\u0435'), ('inactive', '\u041d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0435'), ('waiting', '\u041e\u0436\u0438\u0434\u0430\u0435\u0442 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f'), ('closed', '\u0417\u0430\u043a\u0440\u044b\u0442\u043e\u0435')], default='new', max_length=10, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441'),
        ),
    ]
