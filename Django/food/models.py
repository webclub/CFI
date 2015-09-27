import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from django.utils.timezone import now

class TimeStampedModel(models.Model):
    """ TimeStampedModel
    An abstract base class model that provides self-managed "created" and
    "modified" fields.
    """
    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))

    class Meta:
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)
        abstract = True


class Kitchen(models.Model):
    name = models.CharField(max_length=1000)
    latitude = models.FloatField(default=77.8)
    longitude = models.FloatField(default=22.7)

    kitchen_type = models.CharField(max_length=1000)


class School(models.Model):
    name = models.CharField(max_length=1000)
    latitude = models.FloatField(default=77.8)
    longitude = models.FloatField(default=22.7)
    kitchen = models.ForeignKey(Kitchen)


class Item(models.Model):
    name = models.CharField(max_length=100)


class Manager(models.Model):
    user = models.ForeignKey(User)
    kitchen = models.ForeignKey(Kitchen)
    role = models.IntegerField(default=1)


class Teacher(models.Model):
    user = models.ForeignKey(User)
    school = models.ForeignKey(School)

    # role: primary or secondary
    role = models.IntegerField(default=1)


class SchoolConsumption(models.Model):
    school = models.ForeignKey(School)
    item = models.ForeignKey(Item)
    unit_consumed = models.IntegerField(default=0)
    unit_left = models.IntegerField(default=0)
    date = models.DateField()


class Attendance(models.Model):
    school = models.ForeignKey(School)
    primary = models.IntegerField(default=0)
    secondary = models.IntegerField(default=0)
    date = models.DateField()


class Comments(TimeStampedModel):
    school = models.ForeignKey(School)
    comment = models.CharField(max_length=10000)


class Feedback(TimeStampedModel):
    school = models.ForeignKey(School)
    feedback = models.CharField(max_length=10000)


class ExpectedAttendance(TimeStampedModel):
    school = models.ForeignKey(School)
    primary = models.IntegerField(default=0)
    secondary = models.IntegerField(default=0)
    date = models.DateField()


class ExpectedConsumption(TimeStampedModel):
    school = models.ForeignKey(School)
    item = models.ForeignKey(Item)
    consumption = models.IntegerField(default=0)
    date = models.DateField()
