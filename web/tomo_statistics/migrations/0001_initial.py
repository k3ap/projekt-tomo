# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-09 14:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0013_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('courses.course',),
        ),
    ]
