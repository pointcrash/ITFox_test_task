from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.shortcuts import redirect


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='title', default='Заголовок не задан')
    text = models.TextField(default='Пустая новость')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='news',
                               on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.author = self._get_current_user()
        return super().save(*args, **kwargs)

    def _get_current_user(self):
        return User.objects.get(pk=1)

    def get_absolute_url(self):
        return redirect('news_detail', news_pk=self.pk)

    def __str__(self):
        return self.title

