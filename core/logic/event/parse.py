from .base import BaseEvent
from models.models import Event, User
from sqlalchemy.orm import Session
from models.config import engine
from datetime import datetime
from sqlalchemy import select



"""

#SECTION - ==================== Пакет для обработки данных мероприятий ====================

"""

class ParseEvent(BaseEvent):
    """
    Класс для обработки данных мероприятий.
    """
    
    def parse(self, request):
        """
        Данный метод возращает обработанные данные.
        """
        title=request.data['title']
        photo=request.FILES['photo'].read()
        date=datetime.strptime(request.data['date'], '%Y-%m-%d').date()
        with Session(engine) as session:
            users = select(User).where(User.username == request.data['user'])
            user = session.scalar(users).id
        return title, photo, date, user