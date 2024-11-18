from .base import BaseEvent
from models.models import Event, User
from sqlalchemy import select
from models.config import session
from django.forms.models import model_to_dict
import io
from PIL import Image
"""

#SECTION - ==================== Пакет для получения мероприятий ====================

"""

class GetEvents(BaseEvent):
    """
    Класс для получения мероприятий.
    """
    def get(self, request):
        """
        Данный метод получает все мероприятия
        """
        response ={}
        
        try:
            events = session.scalars(select(Event))
            for event in events:
                response[f'Event №{event.id}'] = {'id':event.id,
                                                   'title': event.title,
                                                   'date': event.date,
                                                   'user': event.user_id
                                                   }
        except Exception as e:
            response['status'] = 400
            print(e)
        finally:
            session.close()
        return response 
    

    
    