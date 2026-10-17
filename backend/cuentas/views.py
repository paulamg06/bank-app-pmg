from dataclasses import asdict
from decimal import Decimal
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .application.cuentasAppService import CuentasAppService, CrearCuentaRequestDto

cuentas_service = CuentasAppService()

# Create your views here.
"""
Obtiene todos los saldos de las cuentas. En caso de querer solo una, se indica por parámetro.
Recibe:
    - id (int, opcional)
Devuelve 200:
    - List (caso de todas las cuentas)
        - id (int)
        - nombre (str)
        - saldo (decimal)
        - fecha_actualizacion (datetime)
En caso de que solo se obtenga una cuenta, es ese mismo objeto individual.
"""
@api_view(['GET'])
def obtener_cuentas(request):
    try:
        if not request.user.is_authenticated:
            return Response(
                {"error": "Usuario no autenticado"},
                status=status.HTTP_401_UNAUTHORIZED
            )
    
        id = request.GET.get('id')

        if id is None or id == '':
            result = cuentas_service.obtener_todas_cuentas(request.user)
            return Response(asdict(result), status.HTTP_200_OK)
        
        result = cuentas_service.obtener_cuenta_por_id(id, request.user)
        return Response(asdict(result), status.HTTP_200_OK)


    except Exception as e:
        return Response({"error": "Error interno del servidor {}".format(str(e))}, status.HTTP_500_INTERNAL_SERVER_ERROR)
    

"""
Crea una cuenta.
Recibe:
    - nombre (str)
    - saldo (decimal)
Devuelve 200:
    - id (int)
    - nombre (str)
    - saldo (decimal)
"""
@api_view(['POST'])
def crear_cuenta(request):
    try:
        print(request.user.is_authenticated)
        if not request.user.is_authenticated:
            return Response(
                {"error": "Usuario no autenticado"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        print(type(request.data.get("saldo")))
        
        dto = CrearCuentaRequestDto(
            nombre=request.data.get("nombre"),
            saldo=Decimal(str(request.data.get("saldo")))
        )

        print(request.data)

        result = cuentas_service.crear_cuenta(dto, request.user)
        return Response(asdict(result), status.HTTP_201_CREATED)
    
    except ValueError as e:
        return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        print(e)
        return Response({"error": "Error interno del servidor {}".format(str(e))}, status.HTTP_500_INTERNAL_SERVER_ERROR)


"""
Elimina una cuenta.
Recibe:
    - id (int)
Devuelve:
    - Mensaje indicando que se ha eliminado correctamente.
"""
@api_view(['DELETE'])
def eliminar_cuenta(request, id: int):
    try:
        if not request.user.is_authenticated:
                    return Response(
                        {"error": "Usuario no autenticado"},
                        status.HTTP_401_UNAUTHORIZED
                    )

        result = cuentas_service.eliminar_cuenta(id, request.user)
        return Response(result, status.HTTP_201_CREATED)
    
    except ValueError as e:
        return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({"error": "Error interno del servidor {}".format(str(e))}, status.HTTP_500_INTERNAL_SERVER_ERROR)