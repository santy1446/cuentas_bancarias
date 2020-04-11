from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TypeAccount, StateAccount, Account, Balance, Movimiento, Categoria
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AccountSerializer, StateAccountSerializer, TypeAccountSerializer, BalanaceSerializer, MovimientotSerializer, CategorySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# 

class AccountAPI(generics.ListAPIView):

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        account = Account.objects.get(pk=pk)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        account = Account.objects.get(pk=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StateAccountAPI(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        stateAccount = StateAccount.objects.all()
        serializer = StateAccountSerializer(stateAccount, many=True)
        return Response(serializer.data)

class TypeAccountAPI(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        typeAccount = TypeAccount.objects.all()
        serializer = TypeAccountSerializer(typeAccount, many=True)
        return Response(serializer.data)

class CategoryAPI(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        category = Categoria.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

class BalanceAPI(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        balance = Balance.objects.all()
        serializer = BalanaceSerializer(balance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BalanaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        balance = Balance.objects.get(pk=pk)
        serializer = BalanaceSerializer(balance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        balance = Balance.objects.get(pk=pk)
        balance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MovementAPI(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        movement = Movimiento.objects.all()
        serializer = MovimientotSerializer(movement, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovimientotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movement = Movimiento.objects.get(pk=pk)
        movement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
