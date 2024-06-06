from django.db import models
from django.contrib import auth
from django_resized import ResizedImageField


class Article(models.Model):
    published = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.ForeignKey(
        'auth.User',
        related_name='articles',
        on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    article_image = ResizedImageField(
        size=[1280, 1280],
        crop=['middle', 'center'],
        upload_to='images/',
        force_format='PNG')
    content = models.TextField()
    shares = models.IntegerField(default=0)

    class Meta:
        ordering = ['published']
