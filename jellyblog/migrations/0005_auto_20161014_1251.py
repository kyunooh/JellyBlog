# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-14 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jellyblog', '0004_document_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='is_markdown',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumnail_img/'),
        ),
    ]
