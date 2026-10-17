from django.urls import path
from .views import obtener_cuentas, crear_cuenta, eliminar_cuenta

urlpatterns = [
    path('', obtener_cuentas),
    path('', obtener_cuentas),
    path('crear/', crear_cuenta),
    path('eliminar/<int:id>/', eliminar_cuenta),
]