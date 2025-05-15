from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='finder'),
    path('pesquisar/', views.pesquisar, name='pesquisar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listagem/', views.listagem, name='listagem'),
]



