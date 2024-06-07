from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from articles import views

urlpatterns = [
    path('articles/',
         views.ArticleList.as_view(),
         name='article-list'),
    path('articles/<int:pk>/',
         views.ArticleDetail.as_view(),
         name='article-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
