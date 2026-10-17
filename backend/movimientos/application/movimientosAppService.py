from datetime import datetime
from ..models import Movimiento
from cuentas.application.cuentasAppService import CuentasAppService
from .dtos import CrearMovimientoRequestDto, CrearMovimientoResponseDto, MovimientosResponseDto, ObtenerMovimientosResponseDto, ObtenerTodosResponseDto

class MovimientosAppService:
    def __init__(self):
        self.movimientoManager = Movimiento.objects
        self.cuentaAppService = CuentasAppService()

    def obtener_todos_movimientos(self) -> list[ObtenerMovimientosResponseDto]:
        response = self.movimientoManager.obtener_todos_movimientos().order_by('-fecha', '-id')

        movimientos_fechas = {}

        for movimiento in response:
            fecha = movimiento.fecha.date()

            dto = ObtenerTodosResponseDto(
                    id=movimiento.id,
                    concepto=movimiento.concepto,
                    cantidad=movimiento.cantidad,
                    saldo_antes=movimiento.saldo_antes,
                    saldo_despues=movimiento.saldo_despues,
                    cuenta_id=movimiento.cuenta.id,
                    cuenta_nombre=movimiento.cuenta.nombre
                )

            if fecha not in movimientos_fechas:
                movimientos_fechas[fecha] = [0, []]  # [balance, movimientos]

            movimientos_fechas[fecha][0] += movimiento.cantidad
            movimientos_fechas[fecha][1].append(dto)

        result = [
            ObtenerMovimientosResponseDto(
                fecha=fecha,
                balance=balance,
                movimientos=movimientos
            )
            for fecha, (balance, movimientos) in movimientos_fechas.items()
        ]
        
        return result
    
    
    def obtener_movimiento_por_id(self, id: int) -> MovimientosResponseDto:
        response = self.movimientoManager.obtener_movimiento_por_id(id)
        
        result = MovimientosResponseDto(
            id=response.id,
            concepto=response.concepto,
            cantidad=response.cantidad,
            fecha=response.fecha,
            saldo_antes=response.saldo_antes,
            saldo_despues=response.saldo_despues,
            cuenta_id=response.cuenta.id,
            cuenta_nombre=response.cuenta.nombre
        )
        
        return result
    
    
    def obtener_movimientos_por_cuenta(self, cuenta: int) -> list[ObtenerMovimientosResponseDto]:
        response = self.movimientoManager.obtener_movimientos_por_cuenta(cuenta).order_by('-fecha', '-id')
        
        movimientos_fechas = {}
        
        for movimiento in response:
            fecha = movimiento.fecha.date()

            dto = ObtenerTodosResponseDto(
                    id=movimiento.id,
                    concepto=movimiento.concepto,
                    cantidad=movimiento.cantidad,
                    saldo_antes=movimiento.saldo_antes,
                    saldo_despues=movimiento.saldo_despues,
                    cuenta_id=movimiento.cuenta.id,
                    cuenta_nombre=movimiento.cuenta.nombre
                )

            if fecha not in movimientos_fechas:
                movimientos_fechas[fecha] = [0, []]  # [balance, movimientos]

            movimientos_fechas[fecha][0] += movimiento.cantidad
            movimientos_fechas[fecha][1].append(dto)

        result = [
            ObtenerMovimientosResponseDto(
                fecha=fecha,
                balance=balance,
                movimientos=movimientos
            )
            for fecha, (balance, movimientos) in movimientos_fechas.items()
        ]
        
        return result
    

    def obtener_movimientos_por_fechas(self, fecha_desde: datetime, fecha_hasta: datetime):
        response = self.movimientoManager.obtener_movimientos_por_fecha(fecha_desde, fecha_hasta).order_by('-fecha', '-id')
        
        result = [
            MovimientosResponseDto(
                id=movimiento.id,
                concepto=movimiento.concepto,
                cantidad=movimiento.cantidad,
                fecha=movimiento.fecha,
                saldo_antes=movimiento.saldo_antes,
                saldo_despues=movimiento.saldo_despues,
                cuenta_id=movimiento.cuenta.id,
                cuenta_nombre=movimiento.cuenta.nombre
            )
            for movimiento in response
        ]
        
        return result


    """Saldos[0] -> saldo anterior
    Saldos[1] -> saldo nuevo
    Saldos[2] -> objeto cuenta"""
    def crear_movimiento(self, dto: CrearMovimientoRequestDto) -> CrearMovimientoResponseDto:
        # Actualizamos el saldo de la cuenta
        saldos = self.cuentaAppService.actualizar_saldo(dto.cuenta, dto.cantidad)

        if (len(saldos) != 3):
            raise Exception("Error al actualizar el saldo")

        response = self.movimientoManager.crear_movimiento(saldos[2], dto.concepto, dto.cantidad, dto.fecha, saldos[0], saldos[1])
        
        result = CrearMovimientoResponseDto(
            id=response.id,
            concepto=response.concepto,
            cantidad=response.cantidad,
            fecha=response.fecha,
            cuenta=response.cuenta.id,
            saldo_antes=response.saldo_antes,
            saldo_despues=response.saldo_despues
        )
        
        return result
    

    def eliminar_movimiento(self, id: int) -> dict:
        response = self.movimientoManager.eliminar_movimiento(id)

        self.cuentaAppService.actualizar_saldo(response[0], -response[1])
        
        result = {"result": f"Movimiento {id} eliminado correctamente."}
        return result