from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from v1.models.about import AboutUsModel
from v1.serializers import AboutUsGetSerializer
from v1.utils.i18n import activate_request_language


@api_view(["GET"])
def list_about_us(request):
    activate_request_language(request)
    queryset = AboutUsModel.objects.all()
    serializer = AboutUsGetSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def retrieve_about_us(request, pk: int):
    activate_request_language(request)
    instance = get_object_or_404(AboutUsModel, pk=pk)
    serializer = AboutUsGetSerializer(instance)
    return Response(serializer.data)
