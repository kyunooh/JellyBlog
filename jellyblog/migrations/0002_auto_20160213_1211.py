# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jellyblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=300)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 13, 12, 11, 27, 207153, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
