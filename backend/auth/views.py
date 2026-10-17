from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .application.authAppService import AuthAppService, RegisterUserRequestDto

auth_service = AuthAppService()

"""
Registra un usuario.
Recibe:
    - username (str)
    - email (str)
    - password (str)
    - first_name (str)
    - last_name (str)
Devuelve 200
"""
# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    try:
        dto = RegisterUserRequestDto(
                email=request.data.get("email"),
                username=request.data.get("username"),
                password=request.data.get("password"),
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name")
            )

        auth_service.register_user(dto)
        return Response("Usuario creado correctamente", status=201)

    except ValueError as e:
        print(e)
        return Response({"error": str(e)}, status=400)
    
    except Exception as e:
        return Response({"error": "Error interno del servidor {}".format(str(e))}, status=500)


"""
Valida las credenciales de un usuario.
Recibe:
    - username (str)
    - password (str)
Devuelve 200
"""
# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    try:
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(
                request,
                username=username,
                password=password
            )

        if user is None:
            return Response(
                {"error": "Credenciales incorrectas"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        login(request, user)

        return Response({
            "mensaje": "Login correcto",
            "usuario": user.username
        }, status=200)
    
    except Exception as e:
        print(e)
        return Response({"error": "Error interno del servidor {}".format(str(e))}, status=500)


""""
Comprueba si el usuario está autenticado
"""
@api_view(['GET'])
def actual_user(request):
    return Response({
        "autenticado": request.user.is_authenticated,
        "usuario": request.user.username
    })


"""
Limpia las cookies para deslogear al usuario.
"""
@api_view(['POST'])
@permission_classes([AllowAny])
def logout_user(request):
    request.session.flush()
    return JsonResponse({"mensaje": "Sesión eliminada"})

"""
Obtiene el token CSRF
"""
@ensure_csrf_cookie
def csrf(request):
    return JsonResponse({"mensaje": "CSRF cookie creada"})
