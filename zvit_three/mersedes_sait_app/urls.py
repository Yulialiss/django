from django.urls import path
from .views import home, cataloge, about, product_detail_view, profile_view
from .views import purchase_form_view


urlpatterns = [
    path('', home, name='home'),
    path('catalog/', cataloge, name='catalog'),
    path('about/', about, name='about'),
    path('product/<int:product_id>/', product_detail_view, name='product_detail'),
    path('purchase/<int:product_id>/', purchase_form_view, name='purchase_form'),
    path('profile/', profile_view, name='profile'),  # Імпорт напряму
]
