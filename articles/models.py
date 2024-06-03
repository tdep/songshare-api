from django.db import models


class Article(models.Model):
    published = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    shares = models.IntegerField(default=0)

    class Meta:
        ordering = ['published']
