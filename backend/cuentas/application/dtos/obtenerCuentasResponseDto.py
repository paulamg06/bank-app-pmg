from dataclasses import dataclass
from datetime import datetime
import decimal

@dataclass
class ObtenerCuentasResponseDto:
    id: int
    nombre: str
    saldo: decimal.Decimal
    fecha_creacion: datetime
    fecha_actualizacion: datetime