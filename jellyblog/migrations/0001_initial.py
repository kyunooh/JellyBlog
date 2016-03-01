# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('parent', models.ForeignKey(to='jellyblog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('meta_tag', models.CharField(max_length=150)),
                ('view_count', models.IntegerField(default=0, editable=False)),
                ('public_doc', models.BooleanField()),
                ('category', models.ForeignKey(to='jellyblog.Category')),
            ],
        ),
    ]
