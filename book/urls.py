from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='finder'),
    path('pesquisar/', views.pesquisar, name='pesquisar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listagem/', views.listagem, name='listagem'),
    path('excluir/<int:livro_id>/', views.excluir_livro, name='excluir_livro'),  # <- nova rota
    path('detalhes/<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),
]





