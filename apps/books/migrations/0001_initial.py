# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from django.conf import settings
import apps.books.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('pages', models.IntegerField()),
                ('publish_date', models.DateTimeField()),
                ('description', models.TextField(blank=True, default='')),
                ('price', models.FloatField(default=0.0)),
                ('cover', models.ImageField(default='', max_length=255, upload_to=apps.books.models._path_to_cover)),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('status', models.IntegerField(default=1, choices=[(1, 'Reading'), (2, 'Read')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(to='books.Book')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_book',
            },
        ),
    ]
