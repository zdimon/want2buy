# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 18:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('archive', '0010_auto_20171213_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('url', models.CharField(blank=True, max_length=250, null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0430\u0439\u0442')),
                ('image', models.ImageField(blank=True, null=True, upload_to='offer_images/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('file', models.FileField(blank=True, null=True, upload_to='offer_files/', verbose_name='\u0410\u0442\u0442\u0430\u0447\u043c\u0435\u043d\u0442')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='\u0426\u0435\u043d\u0430')),
                ('status', models.CharField(choices=[('new', '\u041d\u043e\u0432\u043e\u0435'), ('active', '\u0410\u043a\u0442\u0438\u0432\u043d\u043e\u0435'), ('inactive', '\u041d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0435'), ('closed', '\u0417\u0430\u043a\u0440\u044b\u0442\u043e\u0435')], default='message', max_length=10, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u041a\u043e\u0433\u0434\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u043e?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u0410\u0432\u0442\u043e\u0440')),
            ],
        ),
        migrations.CreateModel(
            name='OfferMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='\u041d\u043e\u0432\u0430\u044f \u0446\u0435\u043d\u0430')),
                ('message', models.TextField(verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('file', models.FileField(blank=True, null=True, upload_to='offer_files/', verbose_name='\u0410\u0442\u0442\u0430\u0447\u043c\u0435\u043d\u0442')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.Offer', verbose_name='\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u0410\u0432\u0442\u043e\u0440')),
            ],
        ),
        migrations.AddField(
            model_name='announcement',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='newannouncement',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=19, verbose_name='\u0426\u0435\u043d\u0430'),
        ),
        migrations.AlterField(
            model_name='newannouncement',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=19, verbose_name='\u0426\u0435\u043d\u0430'),
        ),
    ]