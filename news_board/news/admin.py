from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'time_created', )
    list_display_links = ('id', 'title', )
    search_fields = ('title', 'author__username', 'time_created')
