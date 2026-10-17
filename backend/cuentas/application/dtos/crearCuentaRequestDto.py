from dataclasses import dataclass
import decimal

@dataclass
class CrearCuentaRequestDto:
    nombre: str
    saldo: decimal.Decimal = decimal.Decimal('0.0')

    def __post_init__(self):
        if not self.nombre:
            raise ValueError("cuenta es obligatoria")

        if self.saldo < 0:
            raise ValueError("saldo no puede ser negativo")