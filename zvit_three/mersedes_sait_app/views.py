from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    return render(request, 'mersedes_sait_app/home.html')

def cataloge(request):
    car_type = request.GET.get('type')
    if car_type:
        products = Product.objects.filter(car_type=car_type)
    else:
        products = Product.objects.all()

    return render(request, 'mersedes_sait_app/catalog.html', {'products': products})

def about(request):
    return render(request, 'mersedes_sait_app/about.html')

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'mersedes_sait_app/product_detail.html', {'product': product})


def purchase_form_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'mersedes_sait_app/purchase_form.html', {'product': product})


def profile_view(request):
    return render(request, 'mersedes_sait_app/profile.html')