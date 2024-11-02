from rest_framework import serializers
from models.models import Event

class EventSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    photo = serializers.ImageField()
    date = serializers.DateField()
    user_id = serializers.IntegerField()