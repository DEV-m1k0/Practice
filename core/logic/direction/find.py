from .base import BaseDirection
from models.models import Direction
from sqlalchemy.sql import select
from sqlalchemy.orm import Session
from models.config import engine


"""

#SECTION - ===================== Пакет для поиска направлений =====================

"""


class GetDirection(BaseDirection):
    """
    Класс для получения идентификатора направления по имени или имени по идентификатору.<br>
    Пимер инициализации объекта для получения идентификатора направления:
    ```python
    get_direction = GetDirection(name="Имя_направления")
    direction_id = get_direction.get()
    ```
    Пимер инициализации объекта для получения названия направления:
    ```python
    get_direction = GetDirection(id=123)
    direction_name = get_direction.get()
    ```
    """

    def __init__(self, **kwargs) -> None:
        super().__init__()

        # Проверяем переданные значения и устанавливаем их в поля класса
        if len(kwargs) == 1:
            # Пробуем достать name из kwargs
            try:
                self.name = kwargs.pop('name')
            # Если данного ключа нет, то устанавлеваем ему значение None
            except:
                self.name = None
            # Пробуем достать id из kwargs
            try:
                self.id = kwargs.pop('id')
            # Если данного ключа нет, то устанавливаем ему значение None
            except:
                self.id = None
        else:
            exception = 'KEY_ERROR', "Класс должен принимать только одно значание"
            self.__throw_exception(exception)

    def get(self):
        """
        Функция для получения направления
        """

        # Если передано имя направления, ищем его идентификатор
        if self.name:
            id = self.__get_id_by_name(self.name)
            return id
        # Если передан идентификатор направления, ищем его имя
        elif self.id:
            pass

    def __get_id_by_name(self, name: str):
        """
        Функция для получения идентификатора направления по имени
        ```
        Параметры:
        direction(str): Имя направления

        Возвращается:
        int: id
        ```
        """

        # Создаем sql запрос
        directions_sql_row = select(Direction).where(Direction.name == name)

        # Используем сессию для выполнения запроса и получения данных
        with Session(engine) as session:
            # Получаем направление по имени
            direction_obj = session.scalar(directions_sql_row)

        if direction_obj:
            # Возвращаем идентификатор направления
            return direction_obj.id
        else:
            # Создаем новое направление
            create_direction = CreateDirection(name=self.name)
            create_direction.save()

            # Возвращаем идентификатор нового направления
            direction_id = self.get()
            return direction_id




class CreateDirection(BaseDirection):
    """
    Класс для создания нового направления.<br>
    Пример инициализации объекта для создания направления:
    ```python
    create_direction = CreateDirection(name="Имя_направления")
    create_direction.save()
    ```
    """

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def save(self):
        """
        Функция для сохранения направления
        """
        with Session(engine) as session:
            direction = Direction(name=self.name)
            session.add(direction)
            session.commit()



"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""