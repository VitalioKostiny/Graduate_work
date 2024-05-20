from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from users.models import Feedback, User
from measurement.forms import AddMeasurementForm
from measurement.models import Measurement


def add_measurement(request):
    context = dict()
    if request.method == 'POST':
        result = AddMeasurementForm(request.POST)
        if result.is_valid():  # проверка, что все параметры формы корректные
            data = result.cleaned_data  # получаем словарь данных
            note = Measurement()  # создаем измерение и заполняем его данными
            note.user = request.user
            note.weight = data["weight"]
            note.biceps_girth = data["biceps_girth"]
            note.hip_girth = data["hip_girth"]
            note.save()

            Measurement().get_charts(request.user, 500)
            context['comments'] = Feedback.objects.filter(user_receiver=request.user)
            context['receiver_user_id'] = request.user.id
            context['form'] = AddMeasurementForm()
            messages.success(request, 'Измерение успешно добавлено!', 'success')
            return render(request, "measurement/add_measurement.html", context)
    elif request.method == 'GET':
        result = AddMeasurementForm()
        Measurement().get_charts(request.user, 500)
        context['comments'] = Feedback.objects.filter(user_receiver=request.user)
        context['form'] = result
        context['receiver_user_id'] = request.user.id
        return render(request, "measurement/add_measurement.html", context)


def home(request):
    """
    Страница с таблицей пользователей
    :param request:
    :return:
    """
    context = {
        "users": User.objects.all()
    }
    return render(request, f'project/home.html', context)


def user_detail(request, user_id: int):
    """Страница просмотра результатов другого пользователя"""
    current_user = User.objects.filter(id=user_id).first()
    if current_user:
        Measurement().get_charts(current_user, 700)
        context = dict()
        context['comments'] = Feedback.objects.filter(user_receiver__id=user_id)
        context['receiver_user_id'] = user_id
        return render(request, f'measurement/user_detail.html', context)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_feedback(request, user_receiver_id: int):
    if request.method == 'POST':
        item = Feedback()
        item.user_receiver = User.objects.filter(id=user_receiver_id).first()
        item.user_sender = User.objects.filter(id=request.user.id).first()
        item.comment = request.POST["comment"]
        if item.user_receiver and item.user_sender:
            item.save()
            messages.success(request, 'Комментарий успешно добавлен!', 'success')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

