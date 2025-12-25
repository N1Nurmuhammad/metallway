from rest_framework import serializers

from v1.models.about import AboutUsModel


class AboutUsGetSerializer(serializers.ModelSerializer):
    translatable_fields = ("title", "text")

    class Meta:
        model = AboutUsModel
        fields = (
            "id",
            "title",
            "text",
            "icon",
            "created_at",
            "updated_at",
        )
