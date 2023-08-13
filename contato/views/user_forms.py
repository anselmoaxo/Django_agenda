from django.shortcuts import render
from django.contrib import messages
from contato.forms import RegisterForm
from django.shortcuts import render, get_object_or_404, redirect


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuario cadastrado com Sucesso")
            return redirect("contato:index")

    return render(request, "contato/register.html", {"form": form})
