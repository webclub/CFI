# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20150927_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='expectedattendance',
            name='date',
            field=models.DateField(default=datetime.date(2015, 9, 27)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expectedconsumption',
            name='date',
            field=models.DateField(default=datetime.date(2015, 9, 27)),
            preserve_default=False,
        ),
    ]
