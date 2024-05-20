from django import forms

from .models import User


class UserLoginForm(forms.Form):
    """Форма для логина пользователя"""
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'email', 'label': 'email'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите пароль', 'label': 'Пароль'}
        )
    )


class UserRegistrationForm(forms.Form):
    """Форма для регистрации пользователя"""
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'email', 'label': 'email'}
        )
    )
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'ник', 'label': 'Ник'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите пароль', 'label': 'Пароль'}
        )
    )


class ManagerLoginForm(forms.Form):
    """Форма для логина менеджера"""
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'email', 'label': 'email'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите пароль', 'label': 'Пароль'}
        )
    )


class EditProfileForm(forms.ModelForm):
    """Форма для изменения профиля пользователя"""
    class Meta:
        model = User
        fields = ['full_name', 'email', 'image']
        label = {
            'full_name': "Ник",
            'email': 'email',
            'image': 'Фото'
        }

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

