from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
