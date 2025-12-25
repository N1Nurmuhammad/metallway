from rest_framework import serializers

from v1.models.our_clients import OurClientsModel
from .mixins import TranslatableFieldsSerializerMixin


class OurClientsGetSerializer(TranslatableFieldsSerializerMixin):
    translatable_fields = ("name",)

    class Meta:
        model = OurClientsModel
        fields = (
            "id",
            "name",
            "logo",
            "translations",
            "created_at",
            "updated_at",
        )
