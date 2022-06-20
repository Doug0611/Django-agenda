from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class UserAccountForm(forms.Form):
    error_css_class = 'text-danger'
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'title': 'seu sobrenome'
            }
        )
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'title': 'seu sobrenome'
            }
        )
    )
    username = forms.CharField(
        min_length=4,
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'title': 'crie seu nome de usuário'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'title': 'seu melhor email de preferencia',
                'placeholder': 'name@exemple.com'
            }
        )
    )
    password = forms.CharField(
        min_length=6,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'title': 'crie uma senha de sua preferencia',
                'pattern': r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}'
            }
        )
    )
    password_confirm = forms.CharField(
        min_length=6,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'title': 'informe a senha criada',
                'pattern': r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}'
            }
        )
    )

    def clean_username(self):
        user = self.cleaned_data['username']

        if User.objects.filter(username=user).exists():
            raise forms.ValidationError(_('usuário já está sendo utilizado.'))
        return user

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('email já está sendo utilizado.'))
        return email

    def clean_password_confirm(self):
        data = self.cleaned_data

        if data['password'] != data['password_confirm']:
            raise forms.ValidationError(_('as senhas não conferem.'))
        return data['password_confirm']
