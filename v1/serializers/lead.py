from rest_framework import serializers

from v1.models.lead import LeadModel
from v1.models.products import ProductsModel


class LeadGetSerializer(serializers.ModelSerializer):
    # Many-to-many presented as IDs, read-only
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = LeadModel
        fields = "__all__"


class LeadCreateSerializer(serializers.ModelSerializer):
    # Accept a list of product IDs for the many-to-many relation
    products = serializers.PrimaryKeyRelatedField(queryset=ProductsModel.objects.all(), many=True, required=False)

    class Meta:
        model = LeadModel
        fields = ["id", "name", "email", "products", "comment", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
