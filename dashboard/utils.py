from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render


app_name = 'dashboard'


def is_manager(user):
    """Функция проверяет, что пользователь является менеджером"""
    try:
        if not user.is_manager:
            raise Http404
        return True
    except:
        raise Http404


def add(request, form, messages, title, mess_text, to_path, template_file=f"{app_name}/add.html"):
    """Шаблонная функция добавление в таблицу"""
    if request.method == 'POST':
        result = form(request.POST, request.FILES)
        if result.is_valid():  # проверка, что все параметры в переданной форме корректные
            result.save()   # сохраняем в БД
            messages.success(request, mess_text)    # добавляем в сообщения, которые выводятся вверху страницы сообщение об успехе
            return redirect(f"{app_name}:add_{to_path}")  # отображаем страницу
    else:
        result = form()  # если GET запрос, то создаем форму
    context = {'title': title, 'form': result}      # формируем контекста
    return render(request, template_file, context)  # отображаем форму


def index(request, model, template_file, title):
    data = model.objects.all()
    context = {'title': title, 'data': data}
    return render(request, f'{app_name}/{template_file}.html', context)


def edit(request, form, id, messages, mess, title, to_path, template_file=f'{app_name}/edit.html'):
    item = get_object_or_404(form.Meta.model, id=id)
    if request.method == 'POST':
        result = form(request.POST, request.FILES, instance=item)
        if result.is_valid():
            result.save()
            messages.success(request, mess, 'success')
            return redirect(f'{app_name}:{to_path}')
    else:
        result = form(instance=item)
    context = {'title': f'Изменить {title}', 'form': result}
    return render(request, template_file, context)


def delete(request, form, id, messages, mess, to_path):
    form.objects.filter(id=id).delete()
    messages.success(request, mess, 'success')
    return redirect(f'{app_name}:{to_path}')

