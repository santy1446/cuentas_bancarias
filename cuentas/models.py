from django.db import models
import datetime

# models here.
class TypeAccount(models.Model):
	name = models.CharField(max_length=10)

	def __str__(self):
		return self.name

class StateAccount(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name

class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class ExpenseType(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Account(models.Model):
	account_number = models.IntegerField()
	user_id = models.IntegerField()
	type_account = models.ForeignKey(TypeAccount, null=False, on_delete=models.CASCADE)
	state_account = models.ForeignKey(StateAccount, null=False, on_delete=models.CASCADE)
	creation_day = models.DateTimeField(default=datetime.datetime.now())
	activate = models.BooleanField(default=True)

class Balance(models.Model):
	id_account = models.ForeignKey(Account, null=False, on_delete=models.CASCADE)
	id_user = models.IntegerField()
	saldo = models.DecimalField(max_digits=8, decimal_places=0)
	ingresos = models.IntegerField()
	gastos = models.IntegerField()

class Movimiento(models.Model):
    id_account = models.ForeignKey(Account, null=False, on_delete=models.CASCADE)
    id_balance = models.ForeignKey(Balance, null=False, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, null=False, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=8, decimal_places=0)
    fecha = models.DateField(default=datetime.date.today)


