from .base import BaseEvent
from models.models import Event, User
from sqlalchemy import select
from models.config import session
from django.forms.models import model_to_dict
import io
from PIL import Image
"""

#SECTION - ==================== Пакет для удаления мероприятий ====================

"""

class DeleteEvents(BaseEvent):
    """
    Класс для удаления мероприятий.
    """
    def delete(self, request, id):
        """
        Данный метод удаляет все мероприятия
        """
        response ={}
        
        try:
            event = session.scalar(select(Event).where(Event.id == id))
            session.delete(event)
            session.commit()
        except Exception as e:
            response['status'] = 400
            print(e)
        finally:
            session.close()
        return response 
    

    
    