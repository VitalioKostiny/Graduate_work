from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from users.models import User, Feedback
from measurement.models import Measurement
from .forms import (AddUserForm, AddMeasurementForm, AddFeedbackForm,
                    EditUserForm, EditMeasurementForm, EditFeedbackForm)
from .utils import *


# ________________ index _____________
@user_passes_test(is_manager)  # декоратор проверят, что данный пользователь имеет статус менеджера
@login_required     # декоратор проверяет, что пользователь залогинился на сайте
def users(request):
    """Список всех пользователей"""
    return index(request, User, 'users', 'Пользователи')


@user_passes_test(is_manager)
@login_required
def measurements(request):
    return index(request, Measurement, 'measurements', 'Измерения')


@user_passes_test(is_manager)
@login_required
def feedbacks(request):
    return index(request, Feedback, 'feedbacks', 'Отзывы')


# ________________ add _____________
@user_passes_test(is_manager)
@login_required
def add_user(request):
    return add(request, AddUserForm, messages, 'Добавление пользователя', 'Пользователь добавлен!',
               'users')


@user_passes_test(is_manager)
@login_required
def add_measurement(request):
    return add(request, AddMeasurementForm, messages, 'Добавление измерения', 'Измерение добавлено!',
               'measurement')


@user_passes_test(is_manager)
@login_required
def add_feedback(request):
    return add(request, AddFeedbackForm, messages, 'Добавление отзыва', 'Отзыв добавлен!',
               'feedbacks')


# ________________ delete _____________
@user_passes_test(is_manager)
@login_required
def delete_user(request, user_id):
    return delete(request, User, user_id, messages, 'Пользователь был удален!', 'users')


@user_passes_test(is_manager)
@login_required
def delete_measurement(request, measurement_id):
    return delete(request, Measurement, measurement_id, messages, 'Измерение было удалено!', 'measurements')


@user_passes_test(is_manager)
@login_required
def delete_feedback(request, feedback_id):
    return delete(request, Feedback, feedback_id, messages, 'Отзыв был удален!', 'feedbacks')


# ________________ edit _____________
@user_passes_test(is_manager)
@login_required
def edit_user(request, user_id):
    return edit(request, EditUserForm, user_id, messages, 'Пользователь был изменен', 'пользователя', 'users')


@user_passes_test(is_manager)
@login_required
def edit_measurement(request, measurement_id):
    return edit(request, EditMeasurementForm, measurement_id, messages, 'Измерение было изменено', 'измерения', 'measurements')


@user_passes_test(is_manager)
@login_required
def edit_feedback(request, feedback_id):
    return edit(request, EditFeedbackForm, feedback_id, messages, 'Отзыв был удален', 'отзыва', 'feedbacks')
