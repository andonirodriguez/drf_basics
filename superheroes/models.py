from __future__ import unicode_literals

from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    founder = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class SuperHeroe(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    gender = models.CharField(max_length=100, blank=True, default='')
    real_name = models.CharField(max_length=100, blank=True, default='')
    publisher = models.ForeignKey(Publisher)

    class Meta:
        ordering = ('name',)

