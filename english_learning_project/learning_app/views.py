from django.shortcuts import render

def home(request):
    return render(request, 'learning_app/home.html')

def lessons(request):
    return render(request, 'learning_app/lessons.html')
