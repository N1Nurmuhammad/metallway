from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from v1.models.lead import LeadModel
from v1.serializers import LeadGetSerializer
from v1.serializers.lead import LeadCreateSerializer


@swagger_auto_schema(method='post', request_body=LeadCreateSerializer, responses={201: LeadGetSerializer, 400: 'Validation Error'})
@swagger_auto_schema(method='get', responses={200: LeadGetSerializer(many=True)})
@api_view(["GET", "POST"])
def list_leads(request):
    if request.method == "POST":
        serializer = LeadCreateSerializer(data=request.data)
        if serializer.is_valid():
            lead = serializer.save()
            # Return the created lead using the read serializer for consistency
            read_serializer = LeadGetSerializer(lead)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    queryset = LeadModel.objects.all()
    serializer = LeadGetSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def retrieve_lead(request, pk: int):
    instance = get_object_or_404(LeadModel, pk=pk)
    serializer = LeadGetSerializer(instance)
    return Response(serializer.data)
