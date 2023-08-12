<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from contato.forms import ContatoForm
from django.urls import reverse
from contato.models import Contato


def create(request):
    # Esta função é usada para criar um novo contato.

    # Obtém a URL de ação do formulário.
    form_action = reverse('contato:create')

    # Se o método de requisição for POST, então processe os dados do formulário.
    if request.method == 'POST':
        # Cria um novo objeto ContatoForm a partir dos dados da requisição.
        form = ContatoForm(request.POST)

        # Se o formulário for válido, salve o contato e redirecione para a visualização de atualização.
        if form.is_valid():
            contato = form.save()
            return redirect('contato:update', contato_id=contato.pk)

        # Caso contrário, re-renderize o formulário com erros.
        contexto = {
            'form': form,
            'form_action': form_action,
        }
        return render(
            request,
            'contato/create.html', contexto
                      )

    # Se o método de requisição não for POST, então crie um formulário em branco.
    contexto = {
        'form': ContatoForm(),
        'form_action': form_action,
    }

    # Renderize o modelo create.html com o contexto do formulário.
    return render(
        request,
        'contato/create.html', contexto
                  )


def update(request, contato_id):
    contato = get_object_or_404(Contato, pk=contato_id, show=True)
    form_action = reverse('contato:update', args=(contato_id,)
                          )

    # Se o método de requisição for POST, então processe os dados do formulário.
    if request.method == 'POST':
        # Cria um novo objeto ContatoForm a partir dos dados da requisição.
        form = ContatoForm(request.POST, instance=contato)

        # Se o formulário for válido, salve o contato e redirecione para a visualização de atualização.
        if form.is_valid():
            contato = form.save()
            return redirect('contato:update', contato_id=contato.pk)

        # Caso contrário, re-renderize o formulário com erros.
        contexto = {
            'form': form,
            'form_action': form_action,
        }
        return render(
            request,
            'contato/create.html', contexto
                      )

    # Se o método de requisição não for POST, então crie um formulário em branco.
    contexto = {
        'form': ContatoForm(instance=contato),
        'form_action': form_action,
    }

    # Renderize o modelo create.html com o contexto do formulário.
    return render(
        request,
        'contato/create.html', contexto
                  )


def delete(request, contato_id):
    contact = get_object_or_404(
        Contato, pk=contato_id, show=True
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contato:index')

    return render(
        request,
        'contato/contato.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )

=======
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
>>>>>>> cc44d4472d1f6704bbd8b5bcfbd4b1d3140c35fa
