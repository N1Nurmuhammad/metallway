from rest_framework import serializers

from v1.models.about import AboutUsModel


class AboutUsGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsModel
        fields = "__all__"
