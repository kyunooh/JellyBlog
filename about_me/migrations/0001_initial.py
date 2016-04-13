# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_head', models.CharField(max_length=15)),
                ('second_head', models.CharField(max_length=50)),
                ('first_content', models.TextField()),
                ('second_content', models.TextField()),
                ('image', models.ImageField(upload_to=b'')),
                ('created_datetime', models.TimeField(auto_now_add=True)),
                ('updated_datetime', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('facebook', models.CharField(max_length=250)),
                ('github', models.CharField(max_length=250)),
                ('google', models.CharField(max_length=250)),
                ('twitter', models.CharField(max_length=250)),
                ('instagram', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=150)),
                ('created_datetime', models.TimeField(auto_now_add=True)),
                ('updated_datetime', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ETC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_content', models.TextField()),
                ('second_content', models.TextField()),
                ('thrid_content', models.TextField()),
                ('fourth_content', models.TextField()),
                ('created_datetime', models.TimeField(auto_now_add=True)),
                ('updated_datetime', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logo', models.ImageField(upload_to=b'')),
                ('title', models.CharField(max_length=8)),
                ('first_greet', models.CharField(max_length=50)),
                ('middle_greet', models.TextField()),
                ('last_greet', models.CharField(max_length=150)),
                ('overlay_image', models.ImageField(upload_to=b'')),
                ('created_datetime', models.TimeField(auto_now_add=True)),
                ('updated_datetime', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortFolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_head', models.CharField(max_length=30)),
                ('first_content', models.TextField()),
                ('second_content', models.TextField()),
                ('third_content', models.TextField()),
                ('fourth_content', models.TextField()),
                ('fifth_content', models.TextField()),
                ('sixth_content', models.TextField()),
                ('seventh_content', models.TextField()),
                ('created_datetime', models.TimeField(auto_now_add=True)),
                ('updated_datetime', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usually',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_icon', models.CharField(max_length=50)),
                ('second_icon', models.CharField(max_length=50)),
                ('third_icon', models.CharField(max_length=50)),
                ('first_head', models.CharField(max_length=30)),
                ('second_head', models.CharField(max_length=30)),
                ('thrid_head', models.CharField(max_length=30)),
                ('first_content', models.TextField()),
                ('second_content', models.TextField()),
                ('third_content', models.TextField()),
                ('created_datetime', models.TimeField(auto_now_add=True)),
                ('updated_datetime', models.TimeField(auto_now=True)),
            ],
        ),
    ]
