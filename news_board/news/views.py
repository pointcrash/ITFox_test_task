from django.shortcuts import get_object_or_404, redirect
import datetime
from django.shortcuts import render
import requests

from news.forms import NewsForm
from news.models import News


def news_list(request):
    response = requests.get('http://127.0.0.1:8000/api/news/')
    news = response.json()
    for item in news:
        item['time_created'] = datetime.datetime.strptime(item['time_created'], '%Y-%m-%dT%H:%M:%S.%f%z')
    print(news)

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
        return news.get_absolute_url()
    else:
        form = NewsForm()

    return render(request, 'news_list.html', {'news': news, 'form': form})


def news_detail(request, news_pk):
    try:
        response = requests.get(f'http://127.0.0.1:8000/api/news/{news_pk}')
        news = response.json()
        news['time_created'] = datetime.datetime.strptime(news['time_created'], '%Y-%m-%dT%H:%M:%S.%f%z')
    except:
        return render(request, 'error.html', {'error_message': 'Такой новости не существует'})
    return render(request, 'news_detail.html', {'news': news})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('news_list')
    else:
        form = NewsForm()
