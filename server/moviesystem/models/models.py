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

    reg_id = models.AutoField(max_length=20, null=False, primary_key=True)
    phone = models.CharField(max_length=64, null=False, default='')
    code = models.CharField(max_length=32, null=False, default='')
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'register'
    def __unicode__(self):
        return self.reg_id

class users(models.Model):
     user_id = models.AutoField(max_length=20, null=False, primary_key=True)
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
    movie_id = models.AutoField(max_length=20, null=False, primary_key=True)
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

class mov_peo(models.Model):
    mov_peo_id = models.AutoField(max_length=20, null=False, primary_key=True)
    mov_id = models.BigIntegerField(max_length=20, null=False)
    peo_id = models.BigIntegerField(max_length=20, null=False)
    flag = models.IntegerField(max_length=1, null=True)

    class Meta:
        db_table = 'mov_peo'

    def __unicode__(self):
        return self.mov_peo_id

class people(models.Model):
    peo_id = models.AutoField(max_length=20, null=False, primary_key=True)
    name = models.CharField(max_length=128, null=False)
    gender = models.IntegerField(max_length=1, null=False)
    job = models.TextField(null=True)
    birthday = models.DateTimeField(null=True)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'people'

    def __unicode__(self):
        return self.peo_id

class cinema(models.Model):
    cin_id = models.AutoField(max_length=20, null=False, primary_key=True)
    name = models.CharField(max_length=128, null=False)
    address = models.TextField(null=False)
    description = models.TextField(null=False)
    phone = models.CharField(max_length=64, null=True)
    jobtime = models.TextField(null=True)

    class Meta:
        db_table = 'cinema'

    def __unicode__(self):
        return self.cin_id

class video_hell(models.Model):
    vh_id = models.AutoField(max_length=20, null=False, primary_key=True)
    cin_id = models.BigIntegerField(max_length=20, null=False)
    name = models.CharField(max_length=128, null=True)
    number = models.CharField(max_length=20, null=False)
    screen_size = models.CharField(max_length=32, null=False)

    class Meta:
        db_table = 'video_hell'

    def __unicode__(self):
        return self.vh_id

class video_movie(models.Model):
    vh_mov_id = models.AutoField(max_length=20, null=False, primary_key=True)
    vh_id = models.BigIntegerField(max_length=20, null=False)
    mov_id = models.BigIntegerField(max_length=20, null=False)
    type = models.CharField(max_length=2, null=True)
    starttime = models.DateTimeField(null=False)
    endtime = models.DateTimeField(null=False)
    price = models.BigIntegerField(max_length=20, null=False)

    class Meta:
        db_table = 'video_movie'

    def __unicode__(self):
        return self.vh_mov_id

class seat(models.Model):
    seat_id = models.AutoField(max_length=20, null=False, primary_key=True)
    vh_id = models.BigIntegerField(max_length=20, null=False)
    status = models.IntegerField(default=0)
    row_col = models.CharField(max_length=64, null=False)
    user_id = models.BigIntegerField(max_length=20, null=True)

    class Meta:
        db_table = 'seat'

    def __unicode__(self):
        return self.seat_id


class ticket(models.Model):
    tkt_id = models.AutoField(max_length=20, null=False, primary_key=True)
    user_id = models.BigIntegerField(max_length=20, null=False)
    vh_mov_id = models.BigIntegerField(max_length=20, null=False)
    seat_id = models.BigIntegerField(max_length=20, null=False)
    status = models.IntegerField(default=0)
    create_at = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        db_table = 'ticket'

    def __unicode__(self):
        return self.tkt_id

class cinema_comment(models.Model):
    com_id = models.AutoField(max_length=20, null=False, primary_key=True)
    cin_id = models.BigIntegerField(max_length=20, null=False)
    user_id = models.BigIntegerField(max_length=20, null=False)
    description = models.TextField(null=True)
    create_at = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        db_table = 'cinema_comment'

    def __unicode__(self):
        return self.com_id