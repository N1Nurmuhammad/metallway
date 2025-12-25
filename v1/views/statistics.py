from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from v1.models.statistics import StatisticsModel
from v1.serializers import StatisticsGetSerializer
from v1.utils.i18n import activate_request_language


@api_view(["GET"])
def list_statistics(request):
    activate_request_language(request)
    queryset = StatisticsModel.objects.all()
    serializer = StatisticsGetSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def retrieve_statistics(request, pk: int):
    activate_request_language(request)
    instance = get_object_or_404(StatisticsModel, pk=pk)
    serializer = StatisticsGetSerializer(instance)
    return Response(serializer.data)
