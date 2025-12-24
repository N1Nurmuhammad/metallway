from rest_framework import serializers

from v1.models.statistics import StatisticsModel


class StatisticsGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatisticsModel
        fields = "__all__"
