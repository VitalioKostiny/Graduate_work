from django.urls import path

from measurement import views

app_name = "measurement"


urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add_measurement, name='add_measurement'),
    path('users/<int:user_id>', views.user_detail, name='user_detail'),
    path('add/feedback/<int:user_receiver_id>/', views.add_feedback, name='add_feedback'),
]
