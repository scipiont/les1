from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import logging

logger = logging.getLogger(__name__)

@require_http_methods(["GET"])
def index(request):
    logger.info(f"User with IP: {request.META.get('REMOTE_ADDR')} visited index page.")
    context = {'title': 'Добро пожаловать на мой сайт!',
            'content': 'Здесь вы найдете информацию о моем сайте...'}
    return render(request, 'myapp/index.html', context)

@require_http_methods(["GET"])
def about(request):
    logger.info(f"User with IP: {request.META.get('REMOTE_ADDR')} visited about page.")
    context = {'title': 'Немного обо мне', 
            'content': 'Меня зовут Николай. Я учусь в geekbrains на разработчика Python'}
    return render(request, 'myapp/about.html', context)

#
