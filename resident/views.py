from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, House
from .serializers import HouseSerializer

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])

def add_house(request):
    serializer = HouseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = request.user
    user = get_object_or_404(User, pk=user.pk)
    if user.is_resident:
        House.objects.create(
            house_number=serializer.validated_data['house_number'],
            address=serializer.validated_data['address'],
            user=user
        )
        return  Response(data={"message": "House added successfully"}, status=status.HTTP_201_CREATED)
    return Response(data={"message": "Not Authorized"}, status=status.HTTP_403_FORBIDDEN)