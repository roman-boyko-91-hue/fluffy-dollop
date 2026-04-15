from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)
