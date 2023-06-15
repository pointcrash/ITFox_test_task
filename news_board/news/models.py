from django.db import models
from django.conf import settings


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='title')
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='news',
                               on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.author = self._get_current_user()
        return super().save(*args, **kwargs)

    def _get_current_user(self):
        return getattr(self, 'request', None).user

    def __str__(self):
        return self.title

