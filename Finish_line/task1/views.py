from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import *
from django.core.paginator import Paginator


# Create your views here.

def main(request):
    return render(request, 'main.html')


def games(request):
    games_list = Game.objects.all()
    context = {
        'games_list': games_list
    }
    return render(request, 'games.html', context)


def books(request):
    book1 = 'Хроники Амбера. Р. Желязны'
    book2 = 'Гарри Поттер. Дж. Роулинг'
    book3 = 'Граф Монте-Кристо. А. Дюма'
    context = {
        'books': [book1, book2, book3]
    }
    return render(request, 'books.html', context)


def menu(request):
    return render(request, template_name='menu.html')


def sign_up_by_html(request):
    info = {}
    buyers = Buyer.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        for buyer in buyers:
            if buyer.name == username:
                info['error'] = 'Пользователь уже существует'
                break
        else:
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif not age.isdigit() or int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'

        info.update({
            'username': username,
            'password': password,
            'repeat_password': repeat_password,
            'age': age
        })

        if 'error' in info:
            return render(request, 'registration_page.html',
                          {'info': info})
        Buyer.objects.create(name=username, password=password, age=age)

        return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'registration_page.html', {'info': info})


def sign_up_by_django(request):
    info = {}
    buyers = Buyer.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            for buyer in buyers:
                if buyer.name == username:
                    info['error'] = 'Пользователь уже существует'
                    break
            else:
                if password != repeat_password:
                    info['error'] = 'Пароли не совпадают'
                elif not age.isdigit() or int(age) < 18:
                    info['error'] = 'Вы должны быть старше 18'

            if 'error' in info:
                info.update({
                    'username': username,
                    'password': password,
                    'repeat_password': repeat_password,
                    'age': str(age)
                })
                return render(request, 'registration_page.html',
                              {'form': form, 'info': info})

            Buyer.objects.create(name=username, password=password, age=age)

            return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = ContactForm()
    return render(request, 'registration_page.html',
                  {'form': form}, )


def about_post(request):
    items_per_page = int(request.GET.get('items_per_page', '3'))
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, items_per_page)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    return render(request, 'post.html', {
        'page_posts': page_posts,
        'current_items_per_page': items_per_page,
        'available_items_per_page': ['3', '5', '10', '20'],
    })

