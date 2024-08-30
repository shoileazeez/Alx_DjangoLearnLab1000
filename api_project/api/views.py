from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class BookViewSet(APIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

    def get(self, request):
        # Only authenticated users can access this view
        return Response({'message': 'Hello, authenticated user!'})
# Create your views here.
