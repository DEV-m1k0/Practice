from .base import BaseEvent
from models.models import Event, User
from sqlalchemy import select
from models.config import session
from django.forms.models import model_to_dict
import io
from PIL import Image
"""

#SECTION - ==================== Пакет для получения мероприятий по id ====================

"""

class GetEventbyid(BaseEvent):
    """
    Класс для получения мероприятий по id.
    """
    def get(self, request, id):
        """
        Данный метод получает мероприятие по Id.
        """
        response ={}
        
        try:
            event = session.scalar(select(Event).where(Event.id == id))
            response['Event'] = {'id':event.id,
                                                'title': event.title,
                                                'date': event.date,
                                                'user': event.user_id
                                                }
        except Exception:
            response['status'] = 400
        finally:
            session.close()
        return response 
    

    
    