from django.shortcuts import render
from rest_framework import  generics, response
from logic.event.create import  CreateEvent
from logic.event.get_all import GetEvents
from logic.event.get_by_id import GetEventbyid
from logic.event.update import UpdateEvent
from logic.event.delete import DeleteEvents
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
    
class EventbyidApi(generics.GenericAPIView):
    serializer_class = EventSerializer
    queryset = users_sql = session.scalars(select(Event))
    
    def get(self, request, id):
        resp = GetEventbyid().get(request, id)
        return response.Response(resp)
    
    def put(self, request, id):
        resp = UpdateEvent().update(request, id)
        return response.Response(resp)
    
    def delete(self, request, id):
        resp = DeleteEvents().delete(request, id)
        return response.Response(resp)
