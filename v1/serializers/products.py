from rest_framework import serializers

from v1.models.products import ProductsModel
from .mixins import TranslatableFieldsSerializerMixin


class ProductsGetSerializer(TranslatableFieldsSerializerMixin):
    # Represent related fields in a read-only, ID-based manner for GET usage
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    translatable_fields = ("name", "standard")

    class Meta:
        model = ProductsModel
        fields = (
            "id",
            "name",
            "standard",
            "image",
            "price",
            "category",
            "units",
            "is_in_stock",
            "translations",
            "created_at",
            "updated_at",
        )
