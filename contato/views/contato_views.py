from django.shortcuts import render , get_object_or_404, redirect
from contato.models import Contato
from django.db.models import Q
from django.core.paginator import Paginator


def index(request):
    contatos = Contato.objects.filter(show=True).order_by('-id')
    paginator = Paginator(contatos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    contexto = {
        'page_obj': page_obj,
        'titulo': 'Contatos - ',
    }

    return render(request,
                  'contato/index.html', contexto
                  )


def consulta(request):
    search_value = request.GET.get('q','').strip()
    print(search_value)
    if search_value == '':
        return redirect('contato:index')

    contatos = Contato.objects.filter(show=True)\
        .filter(Q(first_name__icontains=search_value) |
                Q(last_name__icontains=search_value)|
                Q(email__icontains=search_value) |
                Q(phone__icontains=search_value))\
        .order_by('-id')
    paginator = Paginator(contatos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    contexto = {
        'page_obj': page_obj,
        'titulo': 'Contatos - ',
    }

    return render(request,
                  'contato/index.html', contexto
                  )


def contato_detalhe(request, contato_id):
    #contato_unico = Contato.objects.filter(pk=contato_id).first
    #Caso não existir dados retorna 404
    contato_unico = get_object_or_404(
        Contato,pk=contato_id, show= True)

    titulo = f'{contato_unico.first_name} {contato_unico.last_name} - '
    contexto = {
        'contact': contato_unico,
        'titulo': titulo
    }

    return render(request,
                  'contato/contato.html', contexto
                  )



