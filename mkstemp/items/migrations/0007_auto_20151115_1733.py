# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-15 17:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20151115_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_type',
        ),
        migrations.RemoveField(
            model_name='item',
            name='slug',
        ),
    ]
