from django.db import models
from django.conf import settings
from django_resized import ResizedImageField


class Article(models.Model):
    published = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles',
        related_query_name='article',
    )
    description = models.TextField(max_length=1000)
    article_image = ResizedImageField(
        size=[1280, 1280],
        crop=['middle', 'center'],
        upload_to='images/',
        force_format='PNG'
    )
    content = models.TextField()
    shares = models.IntegerField(default=0)

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title
