
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views
from cuentas.views import AccountAPI, StateAccountAPI, TypeAccountAPI, BalanceAPI, MovementAPI, CategoryAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', AccountAPI.as_view(), name = "account"),
    path('account/<int:pk>', AccountAPI.as_view(), name = "account"),
    path('stateAccount/', StateAccountAPI.as_view(), name = "stateAccount"),
    path('typeAccount/', TypeAccountAPI.as_view(), name = "typeAccount"),
    path('balance/', BalanceAPI.as_view(), name = "balance"),
    path('balance/<int:pk>', BalanceAPI.as_view(), name = "balance"),
    path('movement/', MovementAPI.as_view(), name = "movement"),
    path('movement/<int:pk>', MovementAPI.as_view(), name = "movement"),
    path('category/', CategoryAPI.as_view(), name = "category"),
    path('auth-token/', views.obtain_auth_token)

]
