from django.urls import path
from . import views

urlpatterns = [
    path('<int:song_pk>', views.song_detail, name='song_detail')
    path('type/<int:song_type_pk>', views.song_detail, name='songs_with_type')
    ]
