# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-05 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160317_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_moderator',
            field=models.BooleanField(default=False, help_text='Designates whether this user is a moderator or not', verbose_name='active'),
        ),
    ]