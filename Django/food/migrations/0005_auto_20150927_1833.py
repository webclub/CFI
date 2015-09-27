# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20150927_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 27, 18, 33, 54, 548389)),
        ),
        migrations.AlterField(
            model_name='schoolconsumption',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 27, 18, 33, 54, 547802)),
        ),
    ]
