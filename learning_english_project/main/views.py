from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def words(request):
    return render(request, 'main/words.html')

def dictionary(request):
    return render(request, 'main/dictionary.html')

def tests(request):
    return render(request, 'main/tests.html')
