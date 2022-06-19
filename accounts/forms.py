from django import forms


class AccountForm(forms.Form):
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
                'onkeyup': 'isValid()',
                'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}'
            }
        )
    )
