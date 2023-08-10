from django.shortcuts import render, redirect
from contato.forms import ContatoForm


def create(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        contexto = {

            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('contato:create')

        return render(request,
                      'contato/create.html', contexto
                      )
    contexto = {
                'form': ContatoForm()
            }
    return render(request,
                  'contato/create.html', contexto
                  )
