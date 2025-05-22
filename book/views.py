from django.shortcuts import render

def home(request):
    """Renderiza a página inicial."""
    return render(request, 'finder/home.html')

def pesquisar(request):
    """Renderiza a página de pesquisa de livros."""
    return render(request, 'finder/pesquisar.html')

def cadastrar(request):
    """Renderiza a página de cadastro de livros."""
    return render(request, 'finder/cadastrar.html')

def listagem(request):
    """Renderiza a página de listagem de livros."""
    return render(request, 'finder/listagem.html')

def home(request):
    return render(request, 'finder/base.html' )

def home(request):
    return render(request, 'finder/index.html' )
  




