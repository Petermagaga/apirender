from rest_framework.permissions import IsAuthenticated
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Book
from .serializers import BookSerializer
from .permissions import ISAuthorOrReadOnly

# class BookListView(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
#     filterset_fields=['author','published_date']
#     search_fields=['title','author']
#     orderingfields=['published_date']
#     permission_classes = [IsAuthenticated]  # Require authentication

# class BookDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [ISAuthorOrReadOnly]  # Require authentication

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet

class BookViewSet(ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields=['author','published_date']
    search_fields=['title','author']
    ordering_fields=['published_date']
    authentication_classes=[JWTAuthentication]
    permission_classes=[ISAuthorOrReadOnly]


    