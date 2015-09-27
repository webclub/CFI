# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20150927_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 27, 18, 33, 36, 525546)),
        ),
        migrations.AlterField(
            model_name='schoolconsumption',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 27, 18, 33, 36, 524944)),
        ),
    ]
