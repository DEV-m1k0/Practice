from .base import BaseEvent
from models.models import Event
from sqlalchemy.orm import Session
from models.config import engine
from .parse import ParseEvent
from sqlalchemy import select


"""

#SECTION - ==================== Пакет для обновления мероприятий ====================

"""

class UpdateEvent(BaseEvent):
    """
    Класс для обновления мероприятий.
    """
    def update(self, request, id):
        """
        Данный метод обновляет мероприятие
        """
        response ={}
        title, photo, date, user = ParseEvent().parse(request)
        try:
            with Session(engine) as session:
                event = session.scalar(select(Event).where(Event.id == id))
                event.title = title
                event.photo = photo
                event.date = date
                event.user_id = user
                session.commit()
            response['status'] = 200
        except Exception as err:
            response['status'] = 400
            print(err)
        finally:
            session.close()
        return response 
    

    
    