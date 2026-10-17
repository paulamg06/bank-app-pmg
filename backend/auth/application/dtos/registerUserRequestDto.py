from dataclasses import dataclass

@dataclass
class RegisterUserRequestDto:
    email: str
    username: str
    password: str
    first_name: str
    last_name: str

    def __post_init__(self):
        if not self.email:
            raise ValueError("Email es obligatorio")

        if not self.username:
            raise ValueError("Nombre de usuario es obligatorio")

        if not self.password:
            raise ValueError("Password es obligatorio")
        
        if not self.first_name:
            raise ValueError("Nombre es obligatorio")
