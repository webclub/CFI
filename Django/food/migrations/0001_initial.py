# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary', models.IntegerField(default=0)),
                ('secondary', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('kitchen_type', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.IntegerField(default=1)),
                ('kitchen', models.ForeignKey(to='food.Kitchen')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('kitchen', models.ForeignKey(to='food.Kitchen')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolConsumption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_consumed', models.IntegerField(default=0)),
                ('unit_left', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('school', models.ForeignKey(to='food.School')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.IntegerField(default=1)),
                ('school', models.ForeignKey(to='food.School')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='school',
            field=models.ForeignKey(to='food.School'),
        ),
    ]
