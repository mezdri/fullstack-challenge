from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Books
from .serializer import BookSerializer

from bs4 import BeautifulSoup
import request



class BookViewSet(viewsets.ModelViewSet):

    queryset = Books.objects.all()
    serializer_class = BookSerializer


class ScraperView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    def post(self, request):
        return Response({"Ingresamos"},status=200)
