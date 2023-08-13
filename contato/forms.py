from django import forms

from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContatoForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "accept": "image/*",
            }
        )
    )

    class Meta:
        model = models.Contato
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "description",
            "category",
            "picture",
        )


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=10,
        # error_messages={'required': ' Nome é obrigatorio' }
    )
    last_name = forms.CharField(
        required=True,
        min_length=10,
        # error_messages={'required': ' Nome é obrigatorio' }
    )
    email = forms.EmailField(
        required=True,
        # error_messages={'required': ' Nome é obrigatorio' }
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            self.add_error("email", ValidationError("Email já existe ", code="invalid"))
