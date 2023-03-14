from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/<int:anime_id>/', views.anime_detail, name='anime_detail'),
]
