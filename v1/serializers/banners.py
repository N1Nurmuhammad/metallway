from rest_framework import serializers

from v1.models.banners import BannersModel


class BannersGetSerializer(serializers.ModelSerializer):
    translatable_fields = ("title", "text")

    class Meta:
        model = BannersModel
        fields = (
            "id",
            "title",
            "text",
            "background_image",
            "created_at",
            "updated_at",
        )
