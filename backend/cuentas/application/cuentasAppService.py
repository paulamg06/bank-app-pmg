import decimal

from ..models import Cuenta
from .dtos import CrearCuentaRequestDto, CrearCuentaResponseDto, ObtenerCuentasListaResponseDto, ObtenerCuentasResponseDto

class CuentasAppService:
    def __init__(self):
        self.cuentaManager = Cuenta.objects


    def obtener_todas_cuentas(self, user) -> ObtenerCuentasListaResponseDto:
        response = self.cuentaManager.obtener_todas_cuentas(user)

        saldo_total = 0
        lista_cuentas = []

        for elem in response:
            lista_cuentas.append(ObtenerCuentasResponseDto(
                id = elem.id,
                nombre=elem.nombre,
                saldo=elem.saldo,
                fecha_creacion=elem.fecha_creacion,
                fecha_actualizacion=elem.fecha_actualizacion
            ))
            saldo_total += elem.saldo

        result = ObtenerCuentasListaResponseDto(
            saldo_total=saldo_total,
            cuentas=lista_cuentas
        )

        return result
    

    def obtener_cuenta_por_id(self, id: int, user) -> ObtenerCuentasResponseDto:
        response = self.cuentaManager.obtener_cuenta_por_id(id, user)

        result = ObtenerCuentasResponseDto(
            id=response.id,
            nombre=response.nombre,
            saldo=response.saldo,
            fecha_creacion=response.fecha_creacion,
            fecha_actualizacion=response.fecha_actualizacion
        )

        return result


    def crear_cuenta(self, dto: CrearCuentaRequestDto, user) -> CrearCuentaResponseDto:
        print(user)
        response = self.cuentaManager.crear_cuenta(dto.nombre, dto.saldo, user)

        result = CrearCuentaResponseDto(
            id=response.id,
            nombre=response.nombre,
            saldo=response.saldo
        )
        return result
    
    
    def eliminar_cuenta(self, id: int, user) -> dict:
        self.cuentaManager.eliminar_cuenta(id, user)

        result = {"result": f"Cuenta {id} eliminada correctamente."}
        return result
    

    def actualizar_saldo(self, id: int, cantidad: decimal.Decimal) -> list[decimal.Decimal]:
        return self.cuentaManager.actualizar_saldo(id, cantidad)