# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150814_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='institution',
            field=models.CharField(default='Fakulteta za matematiko in fiziko', max_length=140),
            preserve_default=False,
        ),
    ]
