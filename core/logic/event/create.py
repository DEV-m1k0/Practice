from .base import BaseEvent
from models.models import Event, User
from sqlalchemy.orm import Session
from models.config import engine
from datetime import datetime
from sqlalchemy import select
from .parse import ParseEvent



"""

#SECTION - ==================== Пакет для создания мероприятий ====================

"""

class CreateEvent(BaseEvent):
    """
    Класс для получения мероприятий.
    """
    def create(self, request):
        """
        Данный метод создаёт новое мероприятие
        """
        response ={}
        title, photo, date, user = ParseEvent().parse(request)
        try:
            with Session(engine) as session:
                new_event =Event(title=title,
                photo=photo,
                date=date,
                user_id=user)
                session.add(new_event)
                session.commit()
            response['status'] = 200
        except Exception as err:
            response['status'] = 400
            print(err)
        return response 
    

    
    