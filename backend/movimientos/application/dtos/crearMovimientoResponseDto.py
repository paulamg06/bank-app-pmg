from dataclasses import dataclass
import decimal

@dataclass
class CrearMovimientoResponseDto:
    id: int
    concepto: str
    cantidad: decimal.Decimal
    fecha: str 
    cuenta: int
    saldo_antes: decimal.Decimal
    saldo_despues: decimal.Decimal
