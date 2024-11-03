from django.shortcuts import render
from rest_framework import  generics, response
from .logic.events import create_event
from .serializers import EventSerializer

class EventsApi(generics.GenericAPIView):
    serializer_class = EventSerializer
    def post(self, request, *args, **kwargs):
        resp = create_event(request)
        return response.Response(resp)
            
