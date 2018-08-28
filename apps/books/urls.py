from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('books/', views.BookList.as_view(), name="list_books"),
]
