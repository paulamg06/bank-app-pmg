from dataclasses import dataclass
import decimal

@dataclass
class ObtenerTodosResponseDto:
    id: int
    concepto: str
    cantidad: decimal.Decimal
    saldo_antes: decimal.Decimal
    saldo_despues: decimal.Decimal
    cuenta_id: int
    cuenta_nombre: str