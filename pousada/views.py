from rest_framework.decorators import api_view
from rest_framework import status, response
from .  import models
from . import serializers


# 1. Clientes

# Cadastrar Cliente
def cadastrar_cliente(request):
    # Implementar a lógica para cadastrar um novo cliente
    serializer = serializers.ClienteSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return response.Response(serializer.data,status=status.HTTP_201_CREATED)


# Listar Clientes
def listar_clientes(request):
    clientes = models.Cliente.objects.all()  # Listar todos os clientes
    serializer = serializers.ClienteSerializer(clientes,
                                               many=True)  # Converter no formato json (O many serve pra dizer que a consulta retorna mais de um objeto)
    return response.Response(serializer.data)  # Retorna os dados json que o serializer capturou da consulta

# Clientes
@api_view(['GET','POST'])
def clientes(request):
    if request.method == 'POST':
        return cadastrar_cliente(request)
    return listar_clientes(request)





# Buscar Cliente
@api_view(['GET'])
def buscar_cliente(request):
    # Implementar a lógica para buscar um cliente específico
    pass

# 2. Cômodos

# Listar Cômodos
@api_view(['GET'])
def listar_comodos(request):
    # Implementar a lógica para listar todos os cômodos disponíveis
    pass

# Verificar Cômodo
@api_view(['GET'])
def verificar_comodo(request):
    # Implementar a lógica para verificar a disponibilidade de um cômodo
    pass

# 3. Reserva

# Buscar Reserva
@api_view(['GET'])
def buscar_reserva(request):
    # Implementar a lógica para buscar uma reserva específica
    pass

# Incluir Reserva
@api_view(['POST'])
def incluir_reserva(request):
    # Implementar a lógica para incluir uma nova reserva
    pass

# Cancelar Reserva
@api_view(['DELETE'])
def cancelar_reserva(request):
    # Implementar a lógica para cancelar uma reserva existente
    pass

# Alterar Reserva
@api_view(['PUT'])
def alterar_reserva(request):
    # Implementar a lógica para alterar os detalhes de uma reserva
    pass

# 4. Usuário

# Cadastro de Usuário
@api_view(['POST'])
def cadastro_usuario(request):
    # Implementar a lógica para cadastrar um novo usuário
    pass

# Alterar Senha
@api_view(['PUT'])
def alterar_senha(request):
    # Implementar a lógica para alterar a senha de um usuário
    pass

# Desativar Usuário
@api_view(['PUT'])
def desativar_usuario(request):
    # Implementar a lógica para desativar o acesso de um usuário
    pass

# Excluir Usuário
@api_view(['DELETE'])
def excluir_usuario(request):
    # Implementar a lógica para excluir um usuário do sistema
    pass