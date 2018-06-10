# -*- coding: utf-8 -*-
'''
Create on June 8th 2018
@Author KEYS
'''

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=45, null=False, blank=False, primary_key=True)
    password = models.CharField(max_length=45, null=True)
    nike_name = models.TextField(null=False, blank=False)
    avatar_url = models.TextField(null=False, blank=False)
    time_created = models.DateTimeField(auto_now_add=True)
    gender = models.TextField(null=True)
    email = models.CharField(max_length=45, null=True)
    telphone = models.CharField(max_length=11, null=True)
    class Meta:
        db_table = 'msys_user'
    def __unicode__(self):
        return self.user_id

class register(models.Model):

    reg_id = models.BigIntegerField(max_length=20, null=False, default=0, primary_key=True)
    phone = models.CharField(max_length=64, null=False, default='')
    code = models.CharField(max_length=32, null=False, default='')
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'register'
    def __unicode__(self):
        return self.reg_id

class user(models.Model):
     user_id = models.BigIntegerField(max_length=20, null=False, default=0, primary_key=True)
     phone = models.CharField(max_length=64, null=False, default='')
     password = models.CharField(max_length=32, null=False, default='')
     name = models.CharField(max_length=128, null=True)
     pay_num = models.CharField(max_length=64, null=True)
     create_at = models.DateTimeField(auto_now_add=True)

     class Meta:
         db_table = 'user'

     def __unicode__(self):
         return self.user_id

class movie(models.Model):
    movie_id = models.BigIntegerField(max_length=20, null=False, default=0, primary_key=True)
    name = models.CharField(max_length=128, null=True)
    grade = models.FloatField(default=0.0)
    starttime = models.DateTimeField(null=False)
    type = models.TextField(null=True)
    region = models.TextField(null=True)
    language = models.CharField(max_length=32, null=False, default='')
    length = models.IntegerField(null=False, default=0)
    imgUrl = models.TextField(null=True)
    prevueUrl = models.TextField(null=True)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'movie'

    def __unicode__(self):
        return self.movie_id