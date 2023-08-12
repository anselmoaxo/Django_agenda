from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContatoForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept' : 'image/*',
            }
        )
    )

    class Meta:
        model = models.Contato
        fields = ('first_name', 'last_name', 'phone', 'email',
                  'description', 'category', 'picture',
                  )

    def clean(self):
        cleaned_data = self.cleaned_data
