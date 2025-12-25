from rest_framework import serializers

from v1.models.product_category import ProductsCategoryModel
from .mixins import TranslatableFieldsSerializerMixin


class ProductsCategoryGetSerializer(TranslatableFieldsSerializerMixin):
    translatable_fields = ("name",)

    class Meta:
        model = ProductsCategoryModel
        fields = (
            "id",
            "name",
            "image",
            "translations",
            "created_at",
            "updated_at",
        )
