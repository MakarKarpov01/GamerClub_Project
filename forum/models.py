from django.db import models # Импортируем модуль базы данных
from django.contrib.auth.models import User # Подключаем встроенную модель пользователя

class Post(models.Model):
    """Модель сообщения на форуме"""
    
    title = models.CharField('Заголовок', max_length=250) # Заголовок поста
    content = models.TextField('Текст') # Полный текст поста
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='posts')
                            # Автор поста (связь с моделью User)
    created_at = models.DateTimeField(auto_now_add=True) # Дата создания поста

    def __str__(self):
        return self.title[:30] + '...' # Как отображать объект в админке

# Если хочешь добавить категории
class Category(models.Model):
    name = models.CharField('Название раздела', max_length=100)

    def __str__(self):
        return self.name