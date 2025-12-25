from rest_framework import serializers

from v1.models.product_category import ProductsCategoryModel


class ProductsCategoryGetSerializer(serializers.ModelSerializer):
    translatable_fields = ("name",)

    class Meta:
        model = ProductsCategoryModel
        fields = (
            "id",
            "name",
            "image",
            "created_at",
            "updated_at",
        )
