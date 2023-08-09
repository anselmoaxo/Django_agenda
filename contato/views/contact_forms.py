from django.shortcuts import render
from contato.forms import ContatoForm


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
