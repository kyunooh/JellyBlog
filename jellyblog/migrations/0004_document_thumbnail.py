# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jellyblog', '0003_auto_20160331_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='thumbnail',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]