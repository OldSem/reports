# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-02-26 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('everyday', '0009_remove_dte_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='dte',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='everyday.Dept'),
        ),
    ]