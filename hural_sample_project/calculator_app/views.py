from django.shortcuts import render

def calculator(request):
    result = None

    if request.method == 'POST':
        number1 = float(request.POST.get('number1'))
        number2 = float(request.POST.get('number2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = number1 + number2
        elif operation == 'subtract':
            result = number1 - number2
        elif operation == 'multiply':
            result = number1 * number2
        elif operation == 'divide':
            result = number1 / number2

    return render(request, 'calculator_app/calculator.html', {'result': result})
