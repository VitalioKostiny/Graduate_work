from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='users', null=True)
    is_manager = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Feedback(models.Model):
    user_sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_sender', null=True)
    user_receiver = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_receiver', null=True)
    comment = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
