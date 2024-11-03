from base import BaseDirection
from models.models import Direction
from sqlalchemy.sql import select
from sqlalchemy.orm import Session
from models.config import engine


"""

#SECTION - ===================== Пакет для поиска направлений =====================

"""


class GetIdDirection(BaseDirection):
    """
    Класс для получения направления по идентификатору.
    """

    def __init__(self, name: int) -> None:
        super().__init__()
        self.name = name

    def get_id_by_name(self):
        """
        Функция для получения идентификатора направления по имени
        ```
        Параметры:
        direction(str): Имя направления

        Возвращается:
        int: Идентификатор направления
        ```
        """

        # Создаем sql запрос
        directions_sql_row = select(Direction).where(Direction.name == self.name)

        # Используем сессию для выполнения запроса и получения данных
        with Session(engine) as session:
            # Получаем направление по имени
            direction_obj = session.scalar(directions_sql_row)

        if direction_obj:
            # Возвращаем идентификатор направления
            return direction_obj.id
        else:
            # Возвращаем None, если направление не найдено
            return None