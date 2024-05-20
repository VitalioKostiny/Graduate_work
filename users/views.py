from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import UserRegistrationForm, UserLoginForm, ManagerLoginForm, EditProfileForm
from users.models import User


def create_manager():
    """
    Создание менеджера
    """
    if not User.objects.filter(email="manager@example.com").first():
        user = User.objects.create_user(
            "manager@example.com", 'manager', 'managerpass1234'
        )
        # give this user manager role
        user.is_manager = True
        user.save()


def manager_login(request):
    """Обработчик логина менеджера на сайт"""
    if request.method == 'POST':
        form = ManagerLoginForm(request.POST)
        if form.is_valid():  # проверяем, что данные валидные
            data = form.cleaned_data
            user = authenticate(  # проходим аутентификацию
                request, email=data['email'], password=data['password']
            )
            if user is not None and user.is_manager:
                login(request, user)  # заходим на сайт
                return redirect('dashboard:users')
            else:
                messages.error(  # зайти не удалось, создаем сообщение для вывода пользователю
                    request, 'Неверные пароль или почта. Повторите ввод!', 'danger'
                )
                return redirect('users:manager_login')
    else:
        form = ManagerLoginForm()  # создаем форму для отображения
    context = {'form': form}
    return render(request, 'users/manager_login.html', context)


def user_register(request):
    """Регистрация пользователя"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():  # проверяем, что данные валидные
            data = form.cleaned_data
            if not User.objects.filter(email=data['email']):
                user = User.objects.create_user(
                    data['email'], data['full_name'], data['password']
                )
                user.save()
                # создаем сообщение пользователю
                messages.success(request, 'Пользователь успешно зарегистрирован!', 'success')
            else:
                messages.error(
                    request, 'Пользователь с данным  email уже зарегистрирован!', 'danger'
                )
            return redirect('users:user_register')
    else:
        form = UserRegistrationForm()
    context = {'title': 'Регистрация', 'form': form}
    return render(request, 'users/register.html', context)


def user_login(request):
    """Логин пользователя на сайт"""
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():  # проверяем, что данные валидные
            data = form.cleaned_data
            user = authenticate(
                request, email=data['email'], password=data['password']
            )
            if user is not None:
                login(request, user)  # заходим на сайт
                messages.success(request, 'Вы успешно вошли на сайт!', 'success')
                return redirect('measurement:home')
            else:
                messages.error(
                    request, 'Неверные пароль или почта. Повторите ввод!', 'danger'
                )
                return redirect('users:user_login')
    else:
        form = UserLoginForm()
    context = {'title': 'Вход', 'form': form}
    return render(request, 'users/login.html', context)


def user_logout(request):
    """Выход с сайта"""
    logout(request)  # выходим с сайта
    messages.success(request, 'Вы успешно вышли с сайта!', 'success')
    return redirect('users:user_login')


def edit_profile(request):
    """Страница редактирования профиля"""
    form = EditProfileForm(request.POST, request.FILES, instance=request.user)
    if form.is_valid():  # проверяем, что данные валидные
        form.save()  # сохраняем данные
        messages.success(request, 'Данные профиля были успешно обновлены!', 'success')
        return redirect('users:edit_profile')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'title': 'Редактирование профиля', 'form': form}
    return render(request, 'users/edit_profile.html', context)
