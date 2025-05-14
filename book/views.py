from django.shortcuts import render

# Create your views here.

def Listagem(request):
    return render(request, "book/index.html")