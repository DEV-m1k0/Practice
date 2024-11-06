from django.shortcuts import render
from rest_framework import  generics, response
from logic.event.create import  CreateEvent
from logic.event.get_all import GetEvents
from .serializers import EventSerializer
from models.config import session
from models.models import Event, User
from sqlalchemy import select

class EventsApi(generics.GenericAPIView):
    serializer_class = EventSerializer
    queryset = users_sql = session.scalars(select(Event))
    def post(self, request):
        resp = CreateEvent().create(request)
        return response.Response(resp)
    
    def get(self, request):
        resp = GetEvents().get(request)
        return response.Response(resp)
            
