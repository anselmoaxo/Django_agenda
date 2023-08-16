from django.shortcuts import render, redirect, get_object_or_404
from contato.forms import ContatoForm
from django.urls import reverse
from contato.models import Contato
from django.contrib.auth.decorators import login_required


def create(request):
    # Esta função é usada para criar um novo contato.

    # Obtém a URL de ação do formulário.
    form_action = reverse("contato:create")

    # Se o método de requisição for POST, então processe os dados do formulário.
    if request.method == "POST":
        # Cria um novo objeto ContatoForm a partir dos dados da requisição.
        form = ContatoForm(request.POST)

        # Se o formulário for válido, salve o contato e redirecione para a visualização de atualização.
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect("contato:update", contato_id=contact.pk)

        # Caso contrário, re-renderize o formulário com erros.
        contexto = {
            "form": form,
            "form_action": form_action,
        }
        return render(request, "contato/create.html", contexto)

    # Se o método de requisição não for POST, então crie um formulário em branco.
    contexto = {
        "form": ContatoForm(),
        "form_action": form_action,
    }

    # Renderize o modelo create.html com o contexto do formulário.
    return render(request, "contato/create.html", contexto)



@login_required(login_url='contato:login')
def update(request, contato_id):
    contato = get_object_or_404(Contato, pk=contato_id, show=True,
                                owner=request.user)
    form_action = reverse("contato:update", args=(contato_id,))

    # Se o método de requisição for POST, então processe os dados do formulário.
    if request.method == "POST":
        # Cria um novo objeto ContatoForm a partir dos dados da requisição.
        form = ContatoForm(request.POST, instance=contato)

        # Se o formulário for válido, salve o contato e redirecione para a visualização de atualização.
        if form.is_valid():
            contato = form.save()
            return redirect("contato:update", contato_id=contato.pk)

        # Caso contrário, re-renderize o formulário com erros.
        contexto = {
            "form": form,
            "form_action": form_action,
        }
        return render(request, "contato/create.html", contexto)

    # Se o método de requisição não for POST, então crie um formulário em branco.
    contexto = {
        "form": ContatoForm(instance=contato),
        "form_action": form_action,
    }

    # Renderize o modelo create.html com o contexto do formulário.
    return render(request, "contato/create.html", contexto)


def delete(request, contato_id):
    contact = get_object_or_404(Contato, pk=contato_id, show=True,
                                owner=request.user)
    confirmation = request.POST.get("confirmation", "no")

    if confirmation == "yes":
        contact.delete()
        return redirect("contato:index")

    return render(
        request,
        "contato/contato.html",
        {
            "contact": contact,
            "confirmation": confirmation,
        },
    )
