from django.urls import path
from .views import *

app_name = 'hospedagem'

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('hospedagem/listar',HospedagemListar.as_view(),name='hospedagem_listar'),
    path('hospedagem/', HospedagemCriar.as_view(),name='hospedagem_criar'),
    path('hospedagem/detalhar/<int:id>/',HospedagemDetalhar.as_view(), name='hospedagem_detalhar'),
    path('hospedagem/editar/<int:id>/',HospedagemEditar.as_view(), name='hospedagem_editar'),
    path('hospedagem/remover/<int:id>/',HospedagemDeletar.as_view(),name='hospedagem_remover'),
]