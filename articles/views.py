from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework import generics, permissions
from articles.permissions import IsOwnerOrReadOnly
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ArticleForm


class ArticleList(generics.ListCreateAPIView):
    """
    List all articles, or create a new article.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Shows the user


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete an article instance.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

