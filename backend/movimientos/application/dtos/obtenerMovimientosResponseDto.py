from dataclasses import dataclass
from datetime import datetime
import decimal

from .obtenerTodosResponseDto import ObtenerTodosResponseDto

@dataclass
class ObtenerMovimientosResponseDto:
    fecha: datetime
    balance: decimal.Decimal
    movimientos: list[ObtenerTodosResponseDto]