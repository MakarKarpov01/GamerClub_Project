"""GAMERCLUB_PROJECT URL Configuration"""
# -*- coding: utf-8 -*-

from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Здесь важно!
    # Мы подключаем маршруты нашего приложения forum ко всему сайту.
    # Если оставить пустую строку '', главная страница будет форумом.
    # Если написать '/forum/', раздел форума откроется по этому пути.
    path('', include('forum.urls')),
]