from django.urls import path
from . import views

app_name = 'bookstore'

urlpatterns = [
    path('add_author/', views.add_author, name='add_author'),
    path('authors/', views.author_list, name='author_list'),
    path('add_book/', views.add_book, name='add_book'),
    path('books/', views.book_list, name='book_list'),
]
