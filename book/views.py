<<<<<<< HEAD
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
  
=======

def listagem(request):
    livros = Livro.objects.all()
    return render(request, 'book/listagem.html', {'livros': livros})


from django.shortcuts import render, redirect  # type: ignore
from .models import Livro


def home(request):
    return render(request, 'book/index.html')
>>>>>>> 4e54fbf35b030202a4ceae22bc1e1a8fb143fb6f


def pesquisar(request):
    query = request.GET.get('query', '')
    livros = []

    if query:
        livros = Livro.objects.filter(titulo__icontains=query) | Livro.objects.filter(autor__icontains=query)

    return render(request, 'book/pesquisar.html', {'livros': livros, 'query': query})

def cadastrar(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        genero = request.POST.get('genero')
        data_publicacao = request.POST.get('data_publicacao')
        sinopse = request.POST.get('sinopse')

        Livro.objects.create(
            titulo=titulo,
            autor=autor,
            genero=genero,
            data_publicacao=data_publicacao,
            sinopse=sinopse
        )

        return redirect('listagem')  # Redireciona para a página de listagem após cadastrar

    return render(request, 'book/cadastrar.html')


def listagem(request):
    livros = Livro.objects.all()
    return render(request, 'book/listagem.html', {'livros': livros})

def excluir_livro(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    livro.delete()
    return redirect('listagem')

def detalhes_livro(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    return render(request, 'book/detalhes.html', {'livro': livro})

