from django.contrib import admin
from .models import Account, StateAccount, TypeAccount, Balance, Movimiento, Categoria

# Register your models here.
admin.site.register(Account)
admin.site.register(StateAccount)
admin.site.register(TypeAccount)
admin.site.register(Movimiento)
admin.site.register(Categoria)
admin.site.register(Balance)

