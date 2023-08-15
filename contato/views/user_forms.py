from django.shortcuts import render
from django.contrib import messages, auth
from contato.forms import RegisterForm, RegisterUpdateForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuario cadastrado com Sucesso")
            return redirect("contato:index")

    return render(request, "contato/register.html", {"form": form})

@login_required(login_url='contato: login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contato/user_update.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'coontato/user_update.html',
            {
                'form': form
            }
        )

    form.save()
    return redirect('contato:user_update')




def login_view(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form =AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('contato:index')
        messages.error(request, 'Login inválido')

    return render(
        request,
        'contato/login.html',
        {
            'form': form
        }
    )

@login_required(login_url='contato: login')
def logout_view(request):
    auth.logout(request)
    return redirect('contato:login')
