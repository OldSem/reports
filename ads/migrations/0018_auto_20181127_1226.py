# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-11-27 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0017_auto_20181127_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='tegs',
            field=models.ManyToManyField(to='ads.Tags'),
        ),
    ]
