from rest_framework import BookViewSet
from .models import Book
from .serializers import BookSerializer

class MyModelViewSet(BookViewSet.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
