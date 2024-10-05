import random
from django.shortcuts import render

def guess_game(request):
    secret_number = request.session.get('secret_number')
    guesses = request.session.get('guesses', 0)

    if secret_number is None:
        secret_number = random.randint(1, 100)
        request.session['secret_number'] = secret_number
        guesses = 0

    if request.method == "POST":
        guess = int(request.POST.get('guess'))
        guesses += 1
        request.session['guesses'] = guesses

        if guess < secret_number:
            message = "Спробуйте ще раз. Ваше число менше."
        elif guess > secret_number:
            message = "Спробуйте ще раз. Ваше число більше."
        else:
            message = f"Вітаємо! Ви вгадали число {secret_number} за {guesses} спроб!"
            # Скидаємо гру
            del request.session['secret_number']
            del request.session['guesses']
    else:
        message = "Спробуйте вгадати число!"

    return render(request, 'guess_game_app/guess_game.html', {'message': message, 'guesses': guesses})
