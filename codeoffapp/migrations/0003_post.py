# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 01:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codeoffapp', '0002_auto_20171027_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.CharField(max_length=500)),
                ('Posted_On', models.DateField(auto_now=True)),
                ('user_posted', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='codeoffapp.Profile')),
            ],
        ),
    ]
