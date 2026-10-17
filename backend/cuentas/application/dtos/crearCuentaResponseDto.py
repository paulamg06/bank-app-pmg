from dataclasses import dataclass
import decimal

@dataclass
class CrearCuentaResponseDto:
    id: int
    nombre: str
    saldo: decimal.Decimal