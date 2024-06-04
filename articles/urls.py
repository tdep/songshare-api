from django.urls import path
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
