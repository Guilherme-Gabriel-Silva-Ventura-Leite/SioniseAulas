from django.shortcuts import render


def home(request):
    return render(request, 'loja/index.html')


def login_view(request):
    return render(request, 'loja/login.html', {'page_title': 'Entrar'})


def cadastro_view(request):
    return render(request, 'loja/usuario_form.html', {'page_title': 'Criar conta'})


def produto_form_view(request):
    return render(request, 'loja/produto_form.html', {'page_title': 'Novo produto'})
