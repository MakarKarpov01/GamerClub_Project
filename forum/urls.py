# forum/urls.py

from django.urls import path
from . import views  # Импортируем наши функции из views.py

app_name = 'forum'  # Это обязательно для именования маршрутов!

urlpatterns = [
    # Главная страница форума
    path('', views.index, name='index'),
    
    # Страница одного сообщения с ID pk
    # Здесь мы передаём параметр через адресную строку
    path('posts/<int:pk>/', views.post_detail, name='post_detail'), 
]