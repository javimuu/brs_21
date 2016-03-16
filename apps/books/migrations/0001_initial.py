# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('pages', models.IntegerField()),
                ('publish_date', models.DateTimeField()),
                ('description', models.TextField(blank=True, default='')),
                ('price', models.FloatField(default=0.0)),
                ('categories', models.ManyToManyField(to='categories.Category')),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
