# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-22 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('image_path', models.CharField(max_length=100)),
            ],
        ),
    ]
