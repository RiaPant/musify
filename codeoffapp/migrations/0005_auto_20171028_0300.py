# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeoffapp', '0004_post_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Posted_On',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
