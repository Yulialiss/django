from django.shortcuts import render

def hello(request):
    name = None
    greeting = None

    if request.method == "POST":
        name = request.POST.get('name')
        greeting = f"Привіт, {name}!"

    return render(request, 'hello_app/hello.html', {'greeting': greeting, 'name': name})
