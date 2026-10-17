from dataclasses import dataclass
from datetime import datetime
import decimal

@dataclass
class MovimientosResponseDto:
    id: int
    concepto: str
    cantidad: decimal.Decimal
    fecha: datetime
    saldo_antes: decimal.Decimal
    saldo_despues: decimal.Decimal
    cuenta_id: int
    cuenta_nombre: str