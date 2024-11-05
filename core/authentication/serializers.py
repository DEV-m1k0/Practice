from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id_number = serializers.IntegerField()
    password = serializers.CharField(max_length=100)