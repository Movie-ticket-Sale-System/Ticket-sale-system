# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-06-09 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='telphone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
