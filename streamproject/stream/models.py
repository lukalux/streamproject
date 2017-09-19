# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=255)
    sport = models.CharField(max_length=255, default='', blank=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    link = models.CharField(max_length=2000)
    realLink = models.CharField(max_length=2000, blank=True)
    created_at = models.DateField(auto_now=True)
    modified_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
        ordering = ['modified_at']


class PermanentLink(models.Model):
    name = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    realLink = models.CharField(max_length=2000, blank=True)
    created_at = models.DateField(auto_now=True)
    modified_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Permanent Link"
        verbose_name_plural = "Permanent Links"
        ordering = ['name']