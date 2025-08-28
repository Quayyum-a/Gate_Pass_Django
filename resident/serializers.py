from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from resident.models import House, User


class HouseSerializer(serializers.Serializer):
    class Meta:
        model = House
        fields = [ 'house_number', 'address']

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username','first_name', 'last_name', 'email', 'phone', 'password']
