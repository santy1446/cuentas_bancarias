from rest_framework import serializers
from .models import Account, StateAccount, TypeAccount, Balance, Movimiento, Categoria

class BalanaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Balance
		fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = '__all__'

class StateAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = StateAccount
		fields = '__all__'

class TypeAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = TypeAccount
		fields = '__all__'

class MovimientotSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movimiento
		fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = '__all__'



