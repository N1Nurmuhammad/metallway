from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from v1.models.products import ProductsModel
from v1.serializers import ProductsGetSerializer
from v1.utils.i18n import activate_request_language


@api_view(["GET"])
def list_products(request):
    activate_request_language(request)
    queryset = ProductsModel.objects.all()
    serializer = ProductsGetSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def retrieve_products(request, pk: int):
    activate_request_language(request)
    instance = get_object_or_404(ProductsModel, pk=pk)
    serializer = ProductsGetSerializer(instance)
    return Response(serializer.data)
