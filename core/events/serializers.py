from rest_framework import serializers
from models.models import Event, User
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.config import engine

class EventSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    photo = serializers.ImageField()
    date = serializers.DateField()
    try:
        with Session(engine) as session:
            user = select(User.username)
            user_id = serializers.ChoiceField(session.scalars(user).all())
    except:
        pass