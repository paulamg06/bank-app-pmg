from dataclasses import dataclass
from datetime import datetime
import decimal

@dataclass
class CrearMovimientoRequestDto:
    cuenta: int
    concepto: str
    cantidad: decimal.Decimal
    fecha: str 

    def __post_init__(self):
        if not self.cuenta:
            raise ValueError("cuenta es obligatoria")
        if not self.concepto:
            raise ValueError("concepto es obligatorio")
        if not self.fecha:
            self.fecha = datetime.now