# book/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # URL для адмінки
    path('bookstore/', include('bookstore.urls')),  # Підключаємо URL вашого додатка bookstore
]
