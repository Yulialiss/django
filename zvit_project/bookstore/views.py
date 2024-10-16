from django.shortcuts import render, redirect
from .models import Author, Book

def add_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Author.objects.create(name=name)
            return redirect('bookstore:author_list')
    return render(request, 'bookstore/add_author.html')

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'bookstore/author_list.html', {'authors': authors})

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        published_date = request.POST.get('published_date')
        if title and author_id and published_date:
            author = Author.objects.get(id=author_id)
            Book.objects.create(title=title, author=author, published_date=published_date)
            return redirect('bookstore:book_list')
    authors = Author.objects.all()
    return render(request, 'bookstore/add_book.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookstore/book_list.html', {'books': books})
