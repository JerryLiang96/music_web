# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Song, SongType

# Register your models here.


@admin.register(SongType)
class SongTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    ordering = ("id", )


@admin.register(Song)
class Song(admin.ModelAdmin):
    list_display = ('id', 'name', 'singer')
    ordering = ("id", )


# admin.site.register(Song)
