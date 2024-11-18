from rest_framework import  generics, response
from logic.event.create import  CreateEvent
from logic.event.get_all import GetEvents
from logic.event.get_by_id import GetEventbyid
from logic.event.update import UpdateEvent
from logic.event.delete import DeleteEvents
from .serializers import EventSerializer, EventExcelSerializers
from models.config import session
from models.models import Event
from sqlalchemy import select
from logic.event.excel_parse import parse_excel
from models.config import session

class EventsApi(generics.GenericAPIView):
    serializer_class = EventSerializer
    
    def get_queryset(self):
        try:
            users_sql = select(Event)
            queryset = session.scalars(users_sql)
        except:
            queryset = []
        return queryset

    def post(self, request):
        resp = CreateEvent().create(request)
        return response.Response(resp)
    
    def get(self, request):
        resp = GetEvents().get(request)
        return response.Response(resp)
    
class EventbyidApi(generics.GenericAPIView):
    serializer_class = EventSerializer
    
    def get_queryset(self):
        try:
            users_sql = select(Event)
            queryset = session.scalars(users_sql)
        except:
            queryset = []
        return queryset
    
    def get(self, request, id):
        resp = GetEventbyid().get(request, id)
        return response.Response(resp)
    
    def put(self, request, id):
        resp = UpdateEvent().update(request, id)
        return response.Response(resp)
    
    def delete(self, request, id):
        resp = DeleteEvents().delete(request, id)
        return response.Response(resp)
    
class ExcelEvent(generics.GenericAPIView):
    serializer_class = EventExcelSerializers
    
    def post(self, request):
        excel_file = request.FILES['excel']
        events = parse_excel(excel_file)
        print(events)
        if events == "BAD_REQUEST":
            return response.Response({"info": "Пользователи не были добавлены"})
        for event in events:
            title = event['title']
            photo = event['photo']
            date = event['date']
            user_id = event['user_id']
            resp ={}
            try:
                new_event =Event(title=title,
                                 photo=photo,
                                 date=date,
                                 user_id=user_id)
                session.add(new_event)
                resp['status'] = 200
            except Exception as err:
                resp['status'] = 400
                print(err)
        session.commit()
        return response.Response(resp)
