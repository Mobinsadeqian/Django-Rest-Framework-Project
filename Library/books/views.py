from rest_framework import viewsets, permissions, filters
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminReadOnly]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['published_date', 'title']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


