# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-02-26 12:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('everyday', '0011_remove_dte_dept'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dte',
            name='work',
        ),
    ]