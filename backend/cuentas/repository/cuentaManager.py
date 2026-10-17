from datetime import datetime
import decimal

from django.db import models

class CuentaManager(models.Manager):
    def obtener_todas_cuentas(self, user):
        return self.filter(usuario=user)
    

    def obtener_cuenta_por_id(self, id: int, user):
        try:
            cuenta = self.filter(
                id=id,
                usuario=user
            ).first()

            if not cuenta:
                raise ValueError("La cuenta {} no existe o no pertenece al usuario".format(id))

            return cuenta
        
        except self.model.DoesNotExist:
            raise ValueError("La cuenta {} no existe o no pertenece al usuario".format(id))


    def crear_cuenta(self, nombre: str, saldo: decimal.Decimal, user):
        try:
            if self.filter(nombre=nombre).exists():
                raise ValueError("La cuenta {} ya existe".format(nombre))

            cuenta = self.create(nombre=nombre, saldo=saldo, usuario=user)
            return cuenta

        except Exception as e:
            raise ValueError("Error al crear la cuenta: {}".format(str(e)))


    def eliminar_cuenta(self, id: int, user):
        try:
            cuenta = self.filter(
                id=id,
                usuario=user
            ).first()

            if not cuenta:
                raise ValueError("La cuenta no existe o no pertenece al usuario")

            cuenta.borrado = True
            cuenta.fecha_borrado = datetime.now()
            cuenta.save()
            
        except self.model.DoesNotExist:
            raise ValueError("La cuenta no existe")


    def actualizar_saldo(self, id: int, cantidad: decimal.Decimal) -> list[decimal.Decimal]:
        try:
            response = []

            saldo = self.get(id=id)

            response.append(saldo.saldo)

            saldo.saldo += cantidad
            saldo.save()

            response.append(saldo.saldo)

            response.append(saldo)

            return response

        except self.model.DoesNotExist:
            raise ValueError("La cuenta no existe")