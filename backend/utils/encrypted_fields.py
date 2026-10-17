from decimal import Decimal

from cryptography.fernet import Fernet
from django.conf import settings
from django.db import models


class EncryptedFieldMixin:
    def _get_fernet(self):
        return Fernet(settings.FERNET_KEY.encode())

    def _encrypt(self, value):
        return self._get_fernet().encrypt(
            value.encode("utf-8")
        ).decode("utf-8")

    def _decrypt(self, value):
        return self._get_fernet().decrypt(
            value.encode("utf-8")
        ).decode("utf-8")

    def get_prep_value(self, value):
        if value is None:
            return None

        value = self._serialize_value(value)

        return self._encrypt(value)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None

        value = self._decrypt(value)

        return self._deserialize_value(value)


class EncryptedCharField(EncryptedFieldMixin, models.TextField):

    def _serialize_value(self, value):
        return str(value)

    def _deserialize_value(self, value):
        return value


class EncryptedDecimalField(EncryptedFieldMixin, models.TextField):

    def _serialize_value(self, value):
        return str(
            Decimal(value).quantize(Decimal("0.01"))
        )

    def _deserialize_value(self, value):
        return Decimal(value)