from django.urls import path
from . import views  # Імпорт з поточного модуля 'views'

urlpatterns = [
    path('', views.index, name='home'),
    path('words/', views.words, name='words'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('tests/', views.tests, name='tests'),
]
