# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.utils import encoding
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

from django.contrib.auth.models import User


@python_2_unicode_compatible
class Dept(models.Model):
    name = models.CharField(max_length=200)
    user = models.ManyToManyField(User)
    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Wtype(models.Model):
    name = models.CharField(max_length=200)
    dept = models.ForeignKey(Dept,null=True)
    def __str__(self):
        return self.name


@python_2_unicode_compatible
class WorkCode(models.Model):
    name = models.CharField(max_length=200)
    workcode = models.ForeignKey(Wtype,null=True)
    user = models.ManyToManyField(User)
    def __str__(self):
        return self.name



@python_2_unicode_compatible
class Work(models.Model):
    name = models.CharField(max_length=200)
    workcode = models.ForeignKey(WorkCode,null=True)
    user = models.ManyToManyField(User)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Division(models.Model):
    name = models.CharField(max_length=200)
    user = models.ManyToManyField(User)
    def __str__(self):
        return self.name



@python_2_unicode_compatible
class Contra(models.Model):
    edrpou = models.IntegerField()
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class BTS(models.Model):
    ECP = models.CharField(max_length=20)
    UCN = models.CharField(max_length=30)
    adress = models.CharField(max_length=200)
    dn = models.CharField(max_length=50)
    contra = models.ForeignKey(Contra,null=True)
    class Meta:
        ordering = ['adress']
    def __str__(self):
        return self.adress


@python_2_unicode_compatible
class personel(models.Model):

    Name = models.CharField(max_length=50)
    Position = models.CharField(max_length=50,default='SOME STRING')
    user = models.ManyToManyField(User,null=True)

    def __str__(self):
        return self.Name


@python_2_unicode_compatible
class Car(models.Model):
    dn = models.CharField(unique=True,max_length=8,default='')
    model = models.CharField(max_length=20,default='')
    driver = models.CharField(max_length=20)
    def __str__(self):
        return self.model


def yesterday():
    return timezone.now() - timezone.timedelta(days=1)


@python_2_unicode_compatible
class DTE(models.Model):
    created_date = models.DateTimeField(
        default=yesterday)
    nn = models.IntegerField()
    division = models.ForeignKey(Division,null=True)
    work = models.ForeignKey(Work,null=True)
    adress = models.ForeignKey(BTS,null=True)
    rezult = models.CharField(max_length=10,default=u'выполнено')
    executor = models.ManyToManyField(personel)
    elapsed_time = models.CharField(max_length=5)
    car = models.ForeignKey(Car,null=True)
    note = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return str(self.nn)






class report(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now)
    dte = DTE.nn

# Create your models here.
