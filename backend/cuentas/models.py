from django.db import models
from django.core.exceptions import ValidationError
from .repository.cuentaManager import CuentaManager
from django.contrib.auth.models import User

from utils.encrypted_fields import (
    EncryptedCharField,
    EncryptedDecimalField
)

# Create your models here.
"""Tabla Cuenta. Almacena todos los datos de las cuentas."""
class Cuenta(models.Model):
    id = models.AutoField(primary_key=True)

    nombre = EncryptedCharField()
    saldo = EncryptedDecimalField()

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    borrado = models.BooleanField(default=False)
    fecha_borrado = models.DateTimeField(null=True, blank=True)

    objects = CuentaManager()
    

    def clean(self):
        if self.saldo < 0:
            raise ValidationError("El saldo no puede ser negativo.")