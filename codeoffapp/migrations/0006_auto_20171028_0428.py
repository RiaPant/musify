# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeoffapp', '0005_auto_20171028_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Interest',
            field=models.CharField(choices=[((b'Vocal',), b'Vocal'), ((b'Instrumental',), b'Instrumental')], default=(b'Vocal',), max_length=3),
        ),
    ]
