from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published')
    list_filter = ('author', 'published')


# admin.site.register(Article, ArticleAdmin)
admin.site.unregister(Group)

admin.site.site_header = "Article Admin"
