from django.shortcuts import render
from anime.models import Anime


def home(request):
    animes = Anime.objects.all()
    context = {'animes' : animes}
    return render(request, 'pages/home.html', context)
