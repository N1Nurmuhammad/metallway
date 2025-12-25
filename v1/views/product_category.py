from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from v1.models.product_category import ProductsCategoryModel
from v1.serializers import ProductsCategoryGetSerializer


@api_view(["GET"])
def list_product_categories(request):
    queryset = ProductsCategoryModel.objects.all()
    serializer = ProductsCategoryGetSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def retrieve_product_category(request, pk: int):
    instance = get_object_or_404(ProductsCategoryModel, pk=pk)
    serializer = ProductsCategoryGetSerializer(instance)
    return Response(serializer.data)
