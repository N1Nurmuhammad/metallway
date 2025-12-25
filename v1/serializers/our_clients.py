from rest_framework import serializers

from v1.models.our_clients import OurClientsModel



class OurClientsGetSerializer(serializers.ModelSerializer):
    translatable_fields = ("name",)

    class Meta:
        model = OurClientsModel
        fields = (
            "id",
            "name",
            "logo",
            "created_at",
            "updated_at",
        )
