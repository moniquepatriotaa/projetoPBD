
from django.urls import path
from . import views

urlpatterns = [
    # 1. Clientes
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/<int:cliente_id>/', views.buscar_cliente, name='buscar_cliente'),

    # 2. Cômodos
    path('comodos/', views.listar_comodos, name='listar_comodos'),
    path('comodos/<int:comodo_id>/', views.verificar_comodo, name='verificar_comodo'),

    # 3. Reservas
    path('reservas/', views.incluir_reserva, name='incluir_reserva'),
    path('reservas/<int:reserva_id>/', views.buscar_reserva, name='buscar_reserva'),
    path('reservas/<int:reserva_id>/', views.alterar_reserva, name='alterar_reserva'),
    path('reservas/<int:reserva_id>/cancelar', views.cancelar_reserva, name='cancelar_reserva'),



    # 4. Usuários
    path('usuarios/', views.cadastro_usuario, name='cadastro_usuario'),
    path('usuarios/<int:user_id>/', views.excluir_usuario, name='excluir_usuario'),
    path('usuarios/<int:user_id>/alterar_senha/', views.alterar_senha, name='alterar_senha'),
    path('usuarios/<int:user_id>/desativar_usuario/', views.desativar_usuario, name='desativar_usuario'),

]
