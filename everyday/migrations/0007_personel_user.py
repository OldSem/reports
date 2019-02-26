# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-02-26 09:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('everyday', '0006_dte_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='personel',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]