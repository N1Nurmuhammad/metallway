from rest_framework import serializers

from v1.models.about import AboutUsModel
from .mixins import TranslatableFieldsSerializerMixin


class AboutUsGetSerializer(TranslatableFieldsSerializerMixin):
    translatable_fields = ("title", "text")

    class Meta:
        model = AboutUsModel
        fields = (
            "id",
            "title",
            "text",
            "icon",
            "translations",
            "created_at",
            "updated_at",
        )
