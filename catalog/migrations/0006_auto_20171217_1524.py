# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20171214_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('photo', '255x200', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='\u041a\u0430\u0434\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='catalog_pic/', verbose_name='\u0424\u043e\u0442\u043e'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=150, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Region', verbose_name='\u0420\u0435\u0433\u0438\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=150, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=150, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='parent_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category', verbose_name='\u0411\u0430\u0437\u043e\u0432\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='subsubcategory',
            name='name',
            field=models.CharField(max_length=150, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='subsubcategory',
            name='parent_sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.SubCategory', verbose_name='\u0411\u0430\u0437\u043e\u0432\u0430\u044f \u043f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
    ]