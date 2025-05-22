from django.urls import path
from . import views

app_name = 'finder'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('pesquisar/', views.pesquisar, name='pesquisar'),
    path('listagem/', views.listagem, name='listagem'),
]




