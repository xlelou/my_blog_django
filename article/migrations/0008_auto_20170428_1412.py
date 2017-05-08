# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_chioces'),
    ]

    operations = [
        migrations.CreateModel(
            name='side',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('pub_time', models.DateTimeField(null=True)),
                ('counter', models.IntegerField(default=0)),
                ('tel', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-date_time'],
            },
        ),
        migrations.DeleteModel(
            name='Chioces',
        ),
    ]
