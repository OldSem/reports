# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.utils import encoding
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class Tags(models.Model):

    Teg = models.CharField(unique=True,max_length=50)
    Position = models.CharField(max_length=50,default='SOME STRING')

    def __str__(self):
        return self.Teg

@python_2_unicode_compatible
class Ads(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now)
    tegs = models.ManyToManyField(Tags)
    activ = models.IntegerField()
    text = models.TextField()
    phone = models.CharField(max_length=20)


    def __str__(self):
        return str(self.created_date)
# Create your models here.
