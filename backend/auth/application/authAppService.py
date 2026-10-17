from ..repository.authManager import AuthManager
from .dtos import RegisterUserRequestDto

class AuthAppService:
    def __init__(self):
        self.authManager = AuthManager()

    def register_user(self, user: RegisterUserRequestDto):
        self.authManager.create_user(
            user.username,
            user.email,
            user.password,
            user.first_name,
            user.last_name
        )
        return
