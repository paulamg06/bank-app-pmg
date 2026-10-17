from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from .repository.movimientoManager import MovimientoManager

from utils.encrypted_fields import (
    EncryptedCharField,
    EncryptedDecimalField
)

# Create your models here.
"""Tabla Movimientos. Registra todos los movimientos realizados en las cuentas."""
class Movimiento(models.Model):
    id = models.AutoField(primary_key=True)

    cuenta = models.ForeignKey('cuentas.Cuenta', on_delete=models.DO_NOTHING)

    concepto = EncryptedCharField()
    cantidad = EncryptedDecimalField()

    fecha = models.DateTimeField()

    saldo_antes = EncryptedDecimalField(default=0)
    saldo_despues = EncryptedDecimalField(default=0)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    borrado = models.BooleanField(default=False)
    fecha_borrado = models.DateTimeField(null=True, blank=True)

    objects = MovimientoManager()


    def clean(self):
        if self.fecha > timezone.now():
            raise ValidationError("La fecha no puede ser futura.")