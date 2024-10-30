from django.urls import path
from .views import home, cataloge, about, product_detail_view
from .views import purchase_form_view, book_car,logout,register,login




urlpatterns = [
    path('', home, name='home'),
    path('catalog/', cataloge, name='catalog'),
    path('about/', about, name='about'),
    path('product/<int:product_id>/', product_detail_view, name='product_detail'),
    path('purchase/<int:product_id>/', purchase_form_view, name='purchase_form'),
    path('book_car/<int:product_id>/', book_car, name='book_car'),

    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),

]
