from django import forms
from .models import *
from statsapp import models

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class registration_form(UserCreationForm):
    email = forms.EmailField(
        label = "Email",
        required = True,
    )
    first_name = forms.CharField(label="First Name", max_length=30)
    last_name = forms.CharField(label="Last Name", max_length=30)

    class Meta:
        model = User
        fields = ("username", "email","password1","password2")

    def save(self, commit=True):
        user=super(registration_form,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        # user.first_name=self.first_name
        # user.last_name=self.last_name
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username=forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name':'username'
        })
    )
    password=forms.CharField(
        label="Password",
        max_length=32,
        widget=forms.PasswordInput()
    )
