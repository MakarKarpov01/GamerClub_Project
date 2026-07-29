from django.shortcuts import render, get_object_or_404  # <--- Улучшенный импорт
from forum.models import Post  
# Для отправки правильного статуса при ошибке сервера
from django.views.defaults import server_error


"""
Главная страница форума.
Берёт ВСЕ записи из таблицы Post и отдаёт их в шаблон 'index.html'.
Добавлена обработка ситуации, когда записей нет.
"""
def index(request):
    posts = Post.objects.order_by('created_at')[:20]  # Сортировка от старых к новым

    if not posts.exists():
        # Вместо ошибки 404 лучше показать нормальное сообщение на странице
        return render(
            request,
            "index.html",
            {"posts": [], "no_posts_message": "Пока никто ничего не написал."}
        )
    
    return render(
        request, 
        # Шаблон лежит прямо в /templates/
        'index.html', 
        {'posts': posts}
    )


"""
Обработчик ошибки сервера 500.
Отдаёт простой HTML-шаблон с сообщением об ошибке.
Важно! Django сам отправит статус-код 500, нам нужно только указать путь к шаблону.
"""
def error_500(request):
    return render(
        request,
        'error.html',
        status=500 
    )


"""
Показывает страницу конкретного сообщения.
Принимает ID сообщения через параметр pk.
Используем улучшенную функцию get_object_or_404 для обработки отсутствия поста.
"""
def post_detail(request, pk):
    """
    Функция автоматически вернёт ошибку Http404 (страница не найдена),
    если пост с таким идентификатором не существует.
    """
    post = get_object_or_404(Post, pk=pk)
    
    return render(
        request,
        'post.html',  # Убедись, что этот шаблон создан по пути: /forum/templates/post.html
        {'post': post}
    )