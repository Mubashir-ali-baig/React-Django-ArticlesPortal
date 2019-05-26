from rest_framework import viewsets
from .serializers import ArticleSerializer
from ..models import Article
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

#from rest_framework.generics import DestroyAPIView,UpdateAPIView,CreateAPIView,ListAPIView,RetrieveAPIView

'''class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleUpdateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDestroyView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
'''