from rest_framework import serializers

from v1.models.products import ProductsModel


class ProductsGetSerializer(serializers.ModelSerializer):
    # Represent related fields in a read-only, ID-based manner for GET usage
    category = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProductsModel
        fields = "__all__"
