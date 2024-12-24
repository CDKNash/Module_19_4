from django.shortcuts import render
from django.template.defaultfilters import title
from django.views.generic import TemplateView


# Create your views here.
# task4.view ---------------------------------------------------------------

def platform(request):
    return render(request, 'fourth_task/platform.html')


def game(request):
    games = Game.objects.all()
    title_g = "Игры"
    games = Game.objects.all()
    context = {
        'title_g': title_g,
        'games': games
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    title_p = "Корзина"
    content_p = "Это всё иллюзия и ничего не купите (:"
    context = {
        "title_p": title_p,
        "content_p": content_p
    }
    return render(request, 'fourth_task/cart.html', context)


def menu(request):
    Title = "Главная страница"
    main = "Главная"
    game = "Магазин"
    cart = "Корзина"
    context = {
        'Title': Title,
        'main': main,
        'game': game,
        'cart': cart,
    }
    return render(request, "fourth_task/menu.html", context)


# task5.views --------------------------------------------------------------

from django.shortcuts import render, HttpResponse
from .forms import UserRegister
from .models import *

info = {}


# ------------------------------------------------------------------------------

def sign_up_by_html(request):
    buyers = Buyer.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password != repeat_password:
            info['error'] = "Пароли не совпадают"
        elif age < 18:
            info['error'] = "Вы должны быть старше 18"
        elif username in str(buyers):
            info['error'] = "Пользователь уже существует"
        else:
            Buyer.objects.create(name=username, balance=100, age=age)
            return HttpResponse (f'Приветствуем, {username}!')

    return render(request, 'fifth_task/registration_page.html', info)
