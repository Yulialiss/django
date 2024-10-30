from django.shortcuts import render, redirect, get_object_or_404
from .models import PersonalData
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "Користувач з таким ім'ям або електронною поштою вже існує.")
            return redirect('register')

        user = User.objects.create(username=username, password=password, email=email)
        request.session['user_id'] = user.id
        messages.success(request, "Реєстрація пройшла успішно!")
        return redirect('home')

    return render(request, 'regestracion/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
            request.session['user_id'] = user.id
            messages.success(request, "Авторизація пройшла успішно!")
            return redirect('home')
        except User.DoesNotExist:
            messages.error(request, "Неправильне ім'я користувача або пароль.")
            return redirect('login')

    return render(request, 'regestracion/login.html')


def logout(request):
    request.session.flush()
    messages.success(request, "Вихід успішний!")
    return redirect('home')



def book_car(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        payment_method = request.POST.get('payment_method')

        personal_data = PersonalData(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            payment_method=payment_method
        )
        personal_data.save()
        return redirect('home')

    context = {
        'product': product
    }
    return render(request, 'mersedes_sait_app/purchase_form.html', context)

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


