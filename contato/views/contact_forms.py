from django.shortcuts import render , get_object_or_404, redirect
from contato.models import Contato
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ('first_name', 'last_name', 'phone', 'email',
                  )
def create(request):
    if request.method == 'POST':
        contexto = {
            'form': ContatoForm(request.POST)
        }
        return render(request,
                      'contato/create.html', contexto
                      )
    contexto = {
                'form': ContatoForm()
            }
    return render(request,
                  'contato/create.html', contexto
                  )
