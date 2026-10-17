from dataclasses import asdict
from datetime import datetime
from decimal import Decimal

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .application.movimientosAppService import MovimientosAppService, CrearMovimientoRequestDto

movimientos_service = MovimientosAppService()

# Create your views here.
"""
Obtiene todos los movimientos de las cuentas agrupados por fecha.
No recibe nada.
Devuelve 200:
    - list
        - fecha (datetime)
        - balance (decimal)
        - movimientos (list)
            - id (int)
            - concepto (str)
            - cantidad (decimal)
            - fecha (datetime)
            - saldo_antes (decimal)
            - saldo_despues (decimal)
            - cuenta (int)
"""
@api_view(['GET'])
def obtener_todos_movimientos(request):
    try:
        result = movimientos_service.obtener_todos_movimientos()

        return Response([asdict(movimiento) for movimiento in result], status=200)
    
    except ValueError as e:
        return Response({"error": str(e)}, status=400)
    
    except Exception as e:
        return Response({"error": "Error interno del servidor {}".format(str(e))}, status=500)
    

"""
Obtiene los movimientos de una cuenta en particular agrupados por fecha.
Recibe por query:
    - cuenta (int)
Devuelve 200:
    - list
        - fecha (datetime)
        - balance (decimal)
        - movimientos (list)
            - id (int)
            - concepto (str)
            - cantidad (decimal)
            - fecha (datetime)
            - saldo_antes (decimal)
            - saldo_despues (decimal)
            - cuenta (int)
"""
@api_view(['GET'])
def obtener_movimientos_por_cuenta(request):
    try:
        cuenta = request.GET.get('cuenta')

        result = movimientos_service.obtener_movimientos_por_cuenta(cuenta)

        return Response([asdict(movimiento) for movimiento in result], status=200)
    
    except ValueError as e:
        return Response({"error": str(e)}, status=400)
    
    except Exception as e:
        return Response({"error": "Error interno del servidor {}".format(str(e))}, status=500)
    

"""
Obtiene el detalle de un movimiento en particular.
Recibe por query:
    - id (int)
Devuelve 200:
    - id (int)
    - concepto (str)
    - cantidad (decimal)
    - fecha (datetime)
    - saldo_antes (decimal)
    - saldo_despues (decimal)
    - cuenta (int)
"""
@api_view(['GET'])
def obtener_movimiento_por_id(request):
    try:
        id = request.GET.get('id')

        result = movimientos_service.obtener_movimiento_por_id(id)

        return Response(asdict(result), status=200)
    
    except ValueError as e:
        return Response({"error": str(e)}, status=400)
    
    except Exception as e:
        return Response({"error": "Error interno del servidor {}".format(str(e))}, status=500)


"""
Obtiene los movimientos en un rango de fechas dado.
Recibe por query:
    - fecha_desde (datetime)
    - fecha_hasta (datetime)
Devuelve 200:
    - list
        - id (int)
        - concepto (str)
        - cantidad (decimal)
        - fecha (datetime)
        - saldo_antes (decimal)
        - saldo_despues (decimal)
        - cuenta (int)
"""
@api_view(['GET'])
def obtener_movimientos_por_fechas(request):
    try:
        fecha_desde_str = request.GET.get('fecha_desde')
        fecha_desde = datetime.fromisoformat(fecha_desde_str)
        
        fecha_hasta_str = request.GET.get('fecha_hasta')        
        fecha_hasta = datetime.now()
        if fecha_hasta_str is not None and fecha_hasta_str != '':
            fecha_hasta = datetime.fromisoformat(fecha_hasta_str)

        result = movimientos_service.obtener_movimientos_por_fechas(fecha_desde, fecha_hasta)

        return Response([asdict(movimiento) for movimiento in result], status=200)
    
    except ValueError as e:
        return Response({"error": str(e)}, status=400)
    
    except Exception as e:
        return Response({"error": "Error interno del servidor {}".format(str(e))}, status=500)


"""
Crea un nuevo movimiento, actualizando el saldo de la cuenta correspondiente.
Recibe:
    - cuenta (int)
    - concepto (str)
    - cantidad (decimal)
    - fecha (datetime, opcional)
Devuelve 201:
    - id (int)
    - concepto (str)
    - cantidad (decimal)
    - fecha (datetime)
    - cuenta (int)
    - saldo_antes (decimal)
    - saldo_despues (decimal)
"""
@api_view(['POST'])
def crear_movimiento(request):
    try:
        dto = CrearMovimientoRequestDto(
            cuenta=request.data.get("cuenta"),
            concepto=request.data.get("concepto"),
            cantidad=Decimal(str(request.data.get("cantidad"))),
            fecha=request.data.get("fecha")
        )

        result = movimientos_service.crear_movimiento(dto)

        return Response(asdict(result), status=201)
    
    except ValueError as e:
        return Response({"error": str(e)}, status=400)
    
    except Exception as e:
        return Response({"error": "Error interno del servidor {}".format(str(e))}, status=500)


"""
Elimina un movimiento, actualizando el saldo de la cuenta.
Recibe:
    - id (int)
Devuelve 201:
    - Movimiento {id} eliminado correctamente.
"""
@api_view(['DELETE'])
def eliminar_movimiento(request, id: int):
    try:
        result = movimientos_service.eliminar_movimiento(id)
        
        return Response(result, status=201)
    
    except Exception as e:
        return Response({"error": "Error interno del servidor {}".format(str(e))}, status=500)
