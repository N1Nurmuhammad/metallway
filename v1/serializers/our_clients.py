from rest_framework import serializers

from v1.models.our_clients import OurClientsModel


class OurClientsGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurClientsModel
        fields = "__all__"
