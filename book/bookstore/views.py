# bookstore/views.py

from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Отримуємо всі книги
    return render(request, 'bookstore/book_list.html', {'books': books})
