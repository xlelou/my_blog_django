# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_remove_article_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
