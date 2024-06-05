from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import article_image_view, success
from rest_framework.urlpatterns import format_suffix_patterns
from articles import views

urlpatterns = [
    path('articles/',
         views.ArticleList.as_view(),
         name='article-list'),
    path('articles/<int:pk>/',
         views.ArticleDetail.as_view(),
         name='article-detail'),
    path('image_upload',
         article_image_view,
         name='image_upload'),
    path('success',
         success,
         name='success'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
