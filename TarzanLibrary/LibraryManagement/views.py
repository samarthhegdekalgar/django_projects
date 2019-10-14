from django.shortcuts import render
from .models import Book


def home_page(request):
    books = Book.objects.all().order_by('book_name')
    return render(request, 'LibraryManagement/index.html', {'book': books})
