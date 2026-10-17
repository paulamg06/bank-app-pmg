from django.urls import path
from .views import crear_movimiento, eliminar_movimiento, obtener_todos_movimientos, obtener_movimiento_por_id, obtener_movimientos_por_cuenta, obtener_movimientos_por_fechas

urlpatterns = [
    path('', obtener_todos_movimientos),
    path('cuenta/', obtener_movimientos_por_cuenta),
    path('movimiento/', obtener_movimiento_por_id),
    path('fecha/', obtener_movimientos_por_fechas),
    path('crear/', crear_movimiento),
    path('eliminar/<int:id>/', eliminar_movimiento)
]