from rest_framework import serializers

from v1.models.product_category import ProductsCategoryModel


class ProductsCategoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsCategoryModel
        fields = "__all__"
