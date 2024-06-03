from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from v1 import views

urlpatterns = [
    path('v1/', views.ArticleList.as_view()),
    path('v1/<int:pk>/', views.ArticleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)