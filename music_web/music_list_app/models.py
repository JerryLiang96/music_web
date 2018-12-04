# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SongType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return "<Type: {}>".format(self.type_name)


class Song(models.Model):
    name = models.CharField(max_length=50)
    singer = models.CharField(max_length=10)
    time = models.CharField(max_length=50)
    lyric = models.TextField()
    song_type = models.ForeignKey(SongType, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "<Song: {}>".format(self.name)
