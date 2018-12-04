# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Song, SongType

# Create your views here.


def song_list(request):
    context = {}
    context['songs'] = Song.objects.all()
    return render(request, 'song_list.html', context)


def song_detail(request, song_pk):
    context = {}
    context['song'] = get_object_or_404(Song, pk=song_pk)
    return render(request, 'song_detail.html', context)


def songs_with_type(request, song_type_pk):
    context = {}
    song_type = get_object_or_404(Song, pk=songs_with_type)
    context['songs'] = SongType.objects.filter(song_type=song_type_pk)
    context['song_type'] = song_type
    return render(request, 'songs_with_type.html', context)
