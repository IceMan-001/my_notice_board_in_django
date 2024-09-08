from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash
from my_board.settings import LOGIN_REDIRECT_URL
from .forms import UserRegistrationForm, CustomPasswordChangeForm

User = get_user_model()


def register(request):
    # если нажали кнопку регистрации (метод POST)
    if request.method == 'POST':
        # создаем объект с данными из запроса
        user_form = UserRegistrationForm(request.POST)
        # Валидация формы (правильность введенных данных)
        if user_form.is_valid():
            # Создание объекта с полями формы (без сохранения в БД)
            new_user = user_form.save(commit=False)
            # Хеширование пароля пользователя
            new_user.set_password(user_form.cleaned_data['password'])  # Хеширование пароля
            # Сохранение пользователя в БД
            new_user.save()  # по умолчанию commit=True
            context = {'title': 'Успешная регистрация', 'new_user': new_user}
            return render(request, template_name='users/register_done.html', context=context)

    # Если метод GET - отрисовка страницы регистрации
    user_form = UserRegistrationForm()
    context = {'title': 'Регистрация', 'register_form': user_form}
    return render(request, template_name='users/register.html', context=context)


def log_in(request):
    pass


def log_out(request):
    pass


def user_detail(request, pk):
    pass


def change_password(request):
    pass
