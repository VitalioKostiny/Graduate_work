from django.forms import ModelForm

from users.models import User, Feedback
from measurement.models import Measurement


class AddMeasurementForm(ModelForm):
    """Форма для добавления пользователей"""
    class Meta:
        model = Measurement
        fields = ['user', 'weight', 'hip_girth', 'biceps_girth']  # поля из модели, которые надо выводить в форме
        labels = {      # Указание названий полей на форме при выводе на сайте
            'user': 'Пользователь',
            'weight': 'Вес',
            'hip_girth': 'Охват бедер',
            'biceps_girth': "Обхват бицепса"
        }

    def __init__(self, *args, **kwargs):
        super(AddMeasurementForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'    # применение красивого стиля к каждому полю формы


class AddUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password', 'is_admin', 'image', 'is_manager']
        labels = {
            'full_name': 'Имя',
            'email': 'Email',
            'password': 'Пароль',
            'is_admin': "Админ",
            'image': "Фото",
            'is_manager': "Менеджер"
        }

    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['is_admin'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_manager'].widget.attrs['class'] = 'form-check-input'


class AddFeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['user_sender', 'user_receiver', 'comment']
        labels = {
            'user_sender': 'Комментатор',
            'user_receiver': 'Получатель',
            'comment': 'Комментарий',
        }

    def __init__(self, *args, **kwargs):
        super(AddFeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'full_name', 'is_admin', 'image', 'is_manager']
        labels = {
            'email': 'Email',
            'full_name': "Имя",
            'is_admin': "Админ",
            'image': "Фото",
            'is_manager': "Менеджер",
        }

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['is_admin'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_manager'].widget.attrs['class'] = 'form-check-input'


class EditMeasurementForm(ModelForm):
    class Meta:
        model = Measurement
        fields = ['user', 'weight', 'hip_girth', 'biceps_girth']
        labels = {
            'user': 'Пользватель',
            'weight': 'Вес',
            'hip_girth': 'Охват бедер',
            'biceps_girth': "Обхват бицепса"
        }

    def __init__(self, *args, **kwargs):
        super(EditMeasurementForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class EditFeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['user_sender', 'user_receiver', 'comment']
        labels = {
            'user_sender': 'Комментатор',
            'user_receiver': "Получатель",
            'comment': "Комментарий",
        }

    def __init__(self, *args, **kwargs):
        super(EditFeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
