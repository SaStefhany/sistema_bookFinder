from django.urls import path # type: ignore
from . import views

app_name = 'finder'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('pesquisar/', views.pesquisar, name='pesquisar'),
    path('listagem/', views.listagem, name='listagem'),
    path('excluir/<int:livro_id>/', views.excluir_livro, name='excluir_livro'),  # <- nova rota
    path('detalhes/<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),
]




<<<<<<< HEAD
=======

>>>>>>> 4e54fbf35b030202a4ceae22bc1e1a8fb143fb6f
