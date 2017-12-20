# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 15:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20171208_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='\u0421\u0447\u0435\u0442'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=150, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.City', verbose_name='\u0413\u043e\u0440\u043e\u0434'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('avatar', '100x100', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='\u041a\u0430\u0434\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='\u0420\u0435\u0439\u0442\u0438\u043d\u0433'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Region', verbose_name='\u0420\u0435\u0433\u0438\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='site',
            field=models.URLField(blank=True, max_length=50, verbose_name='\u0421\u0430\u0439\u0442'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile', verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='content',
            field=models.TextField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='ammount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile', verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
    ]