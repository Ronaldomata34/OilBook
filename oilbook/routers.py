from rest_framework import routers
from apps.books.viewsets import BookViewSet

router = routers.DefaultRouter()

router.register(r'books', BookViewSet)