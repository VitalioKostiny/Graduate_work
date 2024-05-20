from django.contrib import admin
from django.urls import path

from dashboard import views

app_name = "dashboard"

# Пути к страницам панели управления
urlpatterns = [
    # пути для вывода таблиц
    path('users', views.users, name='users'),
    path('measurements', views.measurements, name='measurements'),
    path('feedbacks', views.feedbacks, name='feedbacks'),
    # пути для форм добавления
    path('add_user/', views.add_user, name='add_user'),
    path('add_measurement/', views.add_measurement, name='add_measurement'),
    path('add_feedback/', views.add_feedback, name='add_feedback'),
    # пути для удаления записей
    path('users/delete/<int:user_id>', views.delete_user, name='delete_user'),
    path('measurements/delete/<int:measurement_id>', views.delete_measurement, name='delete_measurement'),
    path('feedbacks/delete/<int:feedback_id>', views.delete_feedback, name='delete_feedback'),
    # пути для редактирования записей
    path('users/edit/<int:user_id>', views.edit_user, name='edit_user'),
    path('measurements/edit/<int:measurement_id>', views.edit_measurement, name='edit_measurement'),
    path('feedbacks/edit/<int:feedback_id>', views.edit_feedback, name='edit_feedback'),
]

