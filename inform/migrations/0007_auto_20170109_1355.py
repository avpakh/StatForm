# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform', '0006_part2_part3_part4'),
    ]

    operations = [
        migrations.AddField(
            model_name='page1',
            name='razdel1_fill',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page1',
            name='razdel2_fill',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page1',
            name='razdel3_fill',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page1',
            name='razdel4_fill',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
