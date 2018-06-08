# -*- coding: utf-8 -*-
'''
    Created by KEYS on June 8th, 2018
'''

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=45, null=False, blank=False, primary_key=True)
    nike_name = models.TextField(null=False, blank=False)
    avatar_url = models.TextField(null=False, blank=False)
    time_created = models.DateTimeField(auto_now_add=True)
    gender = models.TextField(null=True)
    class Meta:
        db_table = 'msys_user'
    def __unicode__(self):
        return self.user_id