from django.urls import path
from .views import guess_game

urlpatterns = [
    path('', guess_game, name='guess_game'),
]
