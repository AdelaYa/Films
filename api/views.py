from rest_framework import generics
from articles.models import Article
from .serializers import ArticleSerializer
from .permissions import IsAuthorOrReadOnly


class FilmApiView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class FilmApiDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
