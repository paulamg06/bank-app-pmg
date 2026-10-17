from django.contrib.auth.models import User

class AuthManager:
    def create_user(self, username: str, email: str, password: str, first_name: str, last_name: str):
        try:
            # Valida si ya existe el usuario
            if User.objects.filter(email=email).exists():
                raise ValueError("El usuario ya existe")

            User.objects.create_user(
                username=username, 
                email=email, 
                password=password,
                first_name=first_name,
                last_name=last_name)

            return
        
        except Exception as e:
            raise ValueError("Error al crear el usuario: {}".format(str(e)))


    def update_user(self, user_id: int, first_name: str, last_name: str) -> User:
        try:
            user = User.objects.get(id=user_id)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return user
        
        except User.DoesNotExist:
            raise ValueError("El usuario con id {} no existe".format(user_id))
        
        except Exception as e:
            raise ValueError("Error al actualizar el usuario: {}".format(str(e)))