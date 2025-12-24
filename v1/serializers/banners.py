from rest_framework import serializers

from v1.models.banners import BannersModel


class BannersGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannersModel
        fields = "__all__"
