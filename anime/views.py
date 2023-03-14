from django.http.response import Http404
from django.shortcuts import render
from anime.models import Anime, Series

def anime_detail(request, anime_id):
    anime = Anime.objects.filter(id = anime_id).first()
    if not anime:
        raise Http404()
    series = Series.objects.filter(anime = anime).all()
    context = {
        'anime' : anime,
        'series' : series,
    }
    return render(request, 'anime/player.html', context)
