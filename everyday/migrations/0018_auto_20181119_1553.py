# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-11-19 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everyday', '0017_auto_20181119_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dte',
            name='rezult',
            field=models.CharField(default='\u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e', max_length=10),
        ),
    ]