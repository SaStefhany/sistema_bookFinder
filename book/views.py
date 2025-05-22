
def listagem(request):
    livros = Livro.objects.all()
    return render(request, 'book/listagem.html', {'livros': livros})


from django.shortcuts import render, redirect  # type: ignore
from .models import Livro


def home(request):
    return render(request, 'book/index.html')


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

