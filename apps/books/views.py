from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Book

# Create your views here.
class BookList(ListView):
	model = Book
	context_object_name = 'bookqs'
	template_name = 'books/books_list.html'

	"""def get_context_data(self, **kwargs):
					context = super().get_context_data(**kwargs)
					context['boss'] = "Ronaldo"
					return context
			"""
