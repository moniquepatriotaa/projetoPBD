from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import status, response
from rest_framework.response import Response
from .serializers import ComodoSerializer, ReservaSerializer, UsuarioSerializer

from .  import models
from . import serializers
from .models import Comodo, Reserva


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
def buscar_cliente(request, cliente_id):
        try:
            cliente = models.Cliente.objects.get(id=cliente_id)  
            serializer = serializers.ClienteSerializer(cliente)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except models.Cliente.DoesNotExist:
            return response.Response(
                {"erro": "Cliente não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )


# 2. Cômodos

# Listar Cômodos
@api_view(['GET'])
def listar_comodos(request):
    comodos = Comodo.objects.all()
    serializer = ComodoSerializer(comodos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Verificar disponibilidade de um cômodo pelo ID
@api_view(['GET'])
def verificar_comodo(request, comodo_id):
    try:
        comodo = Comodo.objects.get(id=comodo_id)
        serializer = ComodoSerializer(comodo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Comodo.DoesNotExist:
        return Response(
            {"erro": "Cômodo não encontrado"},
            status=status.HTTP_404_NOT_FOUND
        )

# 3. Reserva

# Buscar Reserva
@api_view(['GET'])
def buscar_reserva(request, reserva_id):
    try:
        reserva = Reserva.objects.get(id=reserva_id)
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Reserva.DoesNotExist:
        return Response(
            {"erro": "Reserva não encontrada"},
            status=status.HTTP_404_NOT_FOUND
        )

# Incluir Reserva
@api_view(['POST'])
def incluir_reserva(request):
    serializer = ReservaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Cancelar Reserva
@api_view(['PATCH'])
def cancelar_reserva(request, reserva_id):
    try:
        reserva = Reserva.objects.get(id=reserva_id)
        reserva.status = "cancelada"
        reserva.save()
        return Response({"mensagem": "Reserva cancelada com sucesso"}, status=status.HTTP_204_NO_CONTENT)
    except Reserva.DoesNotExist:
        return Response(
            {"erro": "Reserva não encontrada"},
            status=status.HTTP_404_NOT_FOUND
        )

# Alterar Reserva
@api_view(['PUT','PATCH'])
def alterar_reserva(request, reserva_id):
    try:
        reserva = Reserva.objects.get(id=reserva_id)
    except Reserva.DoesNotExist:
        return Response(
            {"erro": "Reserva não encontrada"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ReservaSerializer(reserva, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 4. Usuário

# Cadastro de Usuário
@api_view(['POST'])
def cadastro_usuario(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Alterar Senha
@api_view(['GET', 'PUT'])
def alterar_senha(request, user_id):
    try:
        usuario = User.objects.get(id=user_id)  # Busca o usuário pelo ID
    except User.DoesNotExist:
        return Response({"erro": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    # Se for um GET, apenas retorna os detalhes do usuário
    if request.method == 'GET':
        return Response({"mensagem": "Usuário encontrado", "username": usuario.username}, status=status.HTTP_200_OK)

    # Se for um PUT, altera a senha
    senha_atual = request.data.get("senha_atual")
    nova_senha = request.data.get("nova_senha")

    if not senha_atual or not nova_senha:
        return Response({"erro": "Os campos 'senha_atual' e 'nova_senha' são obrigatórios"}, status=status.HTTP_400_BAD_REQUEST)

    # Verifica se a senha atual está correta
    if not check_password(senha_atual, usuario.password):
        return Response({"erro": "Senha atual incorreta"}, status=status.HTTP_400_BAD_REQUEST)

    # Evita que o usuário defina a mesma senha
    if senha_atual == nova_senha:
        return Response({"erro": "A nova senha não pode ser igual à senha atual"}, status=status.HTTP_400_BAD_REQUEST)

    usuario.set_password(nova_senha)  # Atualiza a senha com criptografia
    usuario.save()

    return Response({"mensagem": "Senha alterada com sucesso"}, status=status.HTTP_200_OK)


# Desativar Usuário
@api_view(['PUT'])
def desativar_usuario(request, user_id):
    try:
        usuario = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response(
            {"erro": "Usuário não encontrado"},
            status=status.HTTP_404_NOT_FOUND
        )

    usuario.is_active = False
    usuario.save()

    return Response(
        {"mensagem": "Usuário desativado com sucesso"},
        status=status.HTTP_200_OK
    )

# Excluir Usuário
@api_view(['DELETE'])
def excluir_usuario(request, user_id):
    try:
        usuario = User.objects.get(id=user_id)
        usuario.delete()
        return Response(
            {"mensagem": "Usuário excluído com sucesso"},
            status=status.HTTP_204_NO_CONTENT
        )
    except User.DoesNotExist:
        return Response(
            {"erro": "Usuário não encontrado"},
            status=status.HTTP_404_NOT_FOUND
        )
