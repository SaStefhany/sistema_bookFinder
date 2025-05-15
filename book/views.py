from django.shortcuts import render

def home(request):
    return render(request, 'finder/home.html')

def pesquisar(request):
    return render(request, 'finder/pesquisar.html')

def cadastrar(request):
    return render(request, 'finder/cadastrar.html')

def listagem(request):
    return render(request, 'finder/listagem.html')

# views.py
def home(request):
    return render(request, 'finder/finder.html')  




