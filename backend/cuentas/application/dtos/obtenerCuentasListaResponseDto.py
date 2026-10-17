from dataclasses import dataclass
from .obtenerCuentasResponseDto import ObtenerCuentasResponseDto

@dataclass
class ObtenerCuentasListaResponseDto:
    saldo_total: int
    cuentas: list[ObtenerCuentasResponseDto]