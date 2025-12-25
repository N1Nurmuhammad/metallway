from rest_framework import serializers

from v1.models.banners import BannersModel
from .mixins import TranslatableFieldsSerializerMixin


class BannersGetSerializer(TranslatableFieldsSerializerMixin):
    translatable_fields = ("title", "text")

    class Meta:
        model = BannersModel
        fields = (
            "id",
            "title",
            "text",
            "background_image",
            "translations",
            "created_at",
            "updated_at",
        )
