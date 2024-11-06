from .base import BaseEvent
from models.models import Event
from sqlalchemy.sql import select
from sqlalchemy.orm import Session
from models.config import engine



"""

#SECTION - ==================== Пакет для поиска мероприятий ====================

"""


class GetEvent(BaseEvent):
    """
    Класс для получения мероприятий.
    """

    def get_all(self):
        """
        Данный метод возращает все мероприятия
        """

        list_events = []

        # Создаем sql запрос
        events_sql_row = select(Event)

        # Используем сессию для выполнения запроса и получения данных
        with Session(engine) as session:
            try:
                # Получаем все мероприятия
                events = session.scalars(events_sql_row).all()
            except:
                events = []

        # Проходимся по всем мероприятиям
        for event in events:
            # Добавляем название мероприятия в список
            list_events.append(event.title)

        return list_events
    

"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""