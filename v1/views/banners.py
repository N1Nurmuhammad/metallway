from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from v1.models.banners import BannersModel
from v1.serializers import BannersGetSerializer


@api_view(["GET"])
def list_banners(request):
    queryset = BannersModel.objects.all()
    serializer = BannersGetSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def retrieve_banners(request, pk: int):
    instance = get_object_or_404(BannersModel, pk=pk)
    serializer = BannersGetSerializer(instance)
    return Response(serializer.data)
