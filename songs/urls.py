from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from songs import views

urlpatterns = [
    path('songs/', views.SongsList.as_view()),
    path('songs/<int:pk>/', views.SongDetail.as_view()),
]
