from django.db import models
from datetime import datetime

class MovimientoManager(models.Manager):
    def obtener_todos_movimientos(self):
        return self.all()
    

    def obtener_movimiento_por_id(self, id: int):
        try:
            movimiento = self.get(id=id)
            return movimiento
        
        except self.model.DoesNotExist:
            raise ValueError("El movimiento con id {} no existe".format(id))
        

    def obtener_movimientos_por_cuenta(self, cuenta: int):
        movimientos = self.filter(cuenta__id=cuenta)
        return movimientos


    def obtener_movimientos_por_fecha(self, fecha_desde: datetime, fecha_hasta: datetime):
        movimientos = self.filter(fecha__gte=fecha_desde, fecha__lt=fecha_hasta)
        
        return movimientos

    def crear_movimiento(self, cuenta, concepto, cantidad, fecha, saldo_antes, saldo_despues):
        movimiento = self.create(cuenta=cuenta, concepto=concepto, cantidad=cantidad, fecha=fecha, saldo_antes=saldo_antes, saldo_despues=saldo_despues)
        return movimiento

    
    def eliminar_movimiento(self, id):
        movimiento = self.get(id=id)

        response = [movimiento.cuenta.id, movimiento.cantidad]

        movimiento.delete()

        print(response)

        return response

    
    def actualizar_movimiento(self, id, cuenta=None, concepto=None, cantidad=None, fecha=None, saldo_antes=None, saldo_despues=None):
        movimiento = self.get(id=id)
        
        if cuenta is not None:
            movimiento.cuenta = cuenta
        if concepto is not None:
            movimiento.concepto = concepto
        if cantidad is not None:
            movimiento.cantidad = cantidad
        if fecha is not None:
            movimiento.fecha = fecha
        if saldo_antes is not None:
            movimiento.saldo_antes = saldo_antes
        if saldo_despues is not None:
            movimiento.saldo_despues = saldo_despues
        
        movimiento.save()