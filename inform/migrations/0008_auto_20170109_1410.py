# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform', '0007_auto_20170109_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page1',
            name='razdel1_fill',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='page1',
            name='razdel2_fill',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='page1',
            name='razdel3_fill',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='page1',
            name='razdel4_fill',
            field=models.NullBooleanField(),
        ),
    ]
