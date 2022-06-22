from .models import Contact
from django import forms


class NewContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('to_show',)

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telephone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'escreva uma breve descrição para o contato'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm',
                    'arial-label': '.form-select-sm example'
                }
            ),
            'profile_picture': forms.FileInput(
                attrs={
                    'class': 'form-control form-control-sm'
                }
            )
        }
