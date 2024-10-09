from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', include('calculator_app.urls')),
    path('guess/', include('guess_game_app.urls')),
    path('hello/', include('hello_app.urls')),
<<<<<<< HEAD
    path('', include('home_app.urls')),
]
=======
    path('', include('home_app.urls')), 
]
>>>>>>> beb7fca584c04289a027045a2abc377d36129d85
