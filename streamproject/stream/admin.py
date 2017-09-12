# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Link, PermanentLink

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'time', 'modified_at')

class PermanentLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'modified_at')

admin.site.register(Link, LinkAdmin)
admin.site.register(PermanentLink, PermanentLinkAdmin)