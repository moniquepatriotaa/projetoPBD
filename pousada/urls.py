
from django.urls import path
from . import views

urlpatterns = [
    # 1. Clientes
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/buscar/', views.buscar_cliente, name='buscar_cliente'),

    # 2. Cômodos
    path('comodos/', views.listar_comodos, name='listar_comodos'),
    path('comodos/verificar/', views.verificar_comodo, name='verificar_comodo'),

    # 3. Reservas
    path('reservas/buscar/', views.buscar_reserva, name='buscar_reserva'),
    path('reservas/incluir/', views.incluir_reserva, name='incluir_reserva'),
    path('reservas/cancelar/', views.cancelar_reserva, name='cancelar_reserva'),
    path('reservas/alterar/', views.alterar_reserva, name='alterar_reserva'),

    # 4. Usuários
    path('usuarios/cadastrar/', views.cadastro_usuario, name='cadastro_usuario'),
    path('usuarios/alterar_senha/', views.alterar_senha, name='alterar_senha'),
    path('usuarios/desativar/', views.desativar_usuario, name='desativar_usuario'),
    path('usuarios/excluir/', views.excluir_usuario, name='excluir_usuario'),
]
