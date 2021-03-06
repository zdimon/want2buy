# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 15:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Replanishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Replanishment_system', models.CharField(choices=[('liqpay', '\u041b\u0438\u043a\u043f\u0435\u0439')], default='liqpay', max_length=150, verbose_name='\u043f\u043b\u0430\u0442\u0435\u0436\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430')),
                ('ammount', models.FloatField(verbose_name='\u0441\u0443\u043c\u043c\u0430')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438')),
                ('status', models.CharField(choices=[('pending', '\u0412 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0435 '), ('success', '\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d'), ('failure', '\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d'), ('error', '\u041e\u0448\u0438\u0431\u043a\u0430'), ('sandbox', '\u0422\u0435\u0441\u0442')], default='pending', max_length=100, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
                ('user_replanishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
