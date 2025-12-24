from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from v1.models.our_clients import OurClientsModel
from v1.serializers import OurClientsGetSerializer


@api_view(["GET"])
def list_our_clients(request):
    queryset = OurClientsModel.objects.all()
    serializer = OurClientsGetSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def retrieve_our_client(request, pk: int):
    instance = get_object_or_404(OurClientsModel, pk=pk)
    serializer = OurClientsGetSerializer(instance)
    return Response(serializer.data)
