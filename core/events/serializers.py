from rest_framework import serializers
from models.models import Event, User
from sqlalchemy import select
from models.config import session

class EventSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    photo = serializers.ImageField()
    date = serializers.DateField()
    user = serializers.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        users_sql = select(User)
        users = session.scalars(users_sql)
        self.fields['user'].choices = users