from rest_framework import viewsets
from .models import Books
from .serializer import BookSerializer

class BookViewSet(viewsets.ModelViewSet):

    queryset = Books.objects.all()
    serializer_class = BookSerializer
