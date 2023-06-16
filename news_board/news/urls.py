from django.urls import path, include
from rest_framework import routers

from news.api import NewsViewSet
from news.views import *


router = routers.DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('news/', news_list, name='news'),
    path('news/<int:news_pk>', news_detail, name='news_detail'),
    path('api/', include(router.urls)),
]
