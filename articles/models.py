from django.db import models
from django.conf import settings


class Article(models.Model):
    published = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='articles', on_delete=models.CASCADE)

    content = models.TextField()
    shares = models.IntegerField(default=0)

    class Meta:
        ordering = ['published']
