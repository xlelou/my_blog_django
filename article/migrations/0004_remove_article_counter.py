# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_counter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='counter',
        ),
    ]
