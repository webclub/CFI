# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django_extensions.db.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_comments_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpectedAttendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('primary', models.IntegerField(default=0)),
                ('secondary', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='ExpectedConsumption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('consumption', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='latitude',
            field=models.FloatField(default=77.8),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='longitude',
            field=models.FloatField(default=22.7),
        ),
        migrations.AlterField(
            model_name='school',
            name='latitude',
            field=models.FloatField(default=77.8),
        ),
        migrations.AlterField(
            model_name='school',
            name='longitude',
            field=models.FloatField(default=22.7),
        ),
        migrations.AddField(
            model_name='expectedconsumption',
            name='item',
            field=models.ForeignKey(to='food.Item'),
        ),
        migrations.AddField(
            model_name='expectedconsumption',
            name='school',
            field=models.ForeignKey(to='food.School'),
        ),
        migrations.AddField(
            model_name='expectedattendance',
            name='school',
            field=models.ForeignKey(to='food.School'),
        ),
        migrations.AddField(
            model_name='schoolconsumption',
            name='item',
            field=models.ForeignKey(default=datetime.datetime(2015, 9, 27, 12, 58, 58, 552175, tzinfo=utc), to='food.Item'),
            preserve_default=False,
        ),
    ]
