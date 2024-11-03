from .base import BaseRole
from models.models import Role
from sqlalchemy.sql import select
from sqlalchemy.orm import Session
from models.config import engine



"""

#SECTION - ======================= Пакет для поиска ролей =======================

"""



class GetRole(BaseRole):
    """
    Класс для получения данных из ролей<br>
    Пример инициализации объекта для получения названия роли:
    ```python
    get_role = GetRole(name="Имя_роли")
    role_name = get_role.get()
    ```
    Пример инициализации обхъекта для получения id роли:
    ```python
    get_role = GetRole(id=123)
    role_id = get_role.get()
    ```
    """
    def __init__(self, **kwargs) -> None:
        super().__init__()
        # Проверяем переданные значения и устанавливаем их в поля класса
        if len(kwargs) == 1:
            # Пробуем достать атрибут name из kwargs
            try:
                self.name = kwargs.pop('name')
            # Если его нет, то устанавливаем self.name = None
            except:
                self.name = None
            # Пробуем достать атрибут id из kwargs
            try:
                self.id = kwargs.pop('id')
            # Если его нет, то устанавливаем self.id = None
            except:
                self.id = None
        # Если аттрибутов несколько, то выкидываем исключение
        else:
            exception = 'KEY_ERROR', "Класс должен принимать только одно значение"
            self.__throw_exception(exception)

    
    def get(self):
        """
        Функция для получения данных ролей
        """
        # Если передано имя роли, ищем его id
        if self.name:
            return self.__get_id_by_role()
        # Если передан идентификатор роли, ищем его имя
        elif self.id:
            return self.__get_role_by_id()
        else:
            exception = 'KEY_ERROR', "Класс должен принимать одно из значений: name или id"
            self.__throw_exception(exception)

    def __get_role_by_id(self):
        pass

    def __get_id_by_role(self):
        """
        Функция для получения идентификатора роли по имени
        ```
        Параметры:
        role(str): Имя роли

        Возвращается:
        int: Идентификатор роли
        ```
        """

        # Создаем sql запрос
        roles_sql_row = select(Role).where(Role.name == self.name)

        # Используем сессию для выполнения запроса и получения данных
        with Session(engine) as session:
            # Получаем роль по имени
            role_obj = session.scalar(roles_sql_row)

        if role_obj:
            # Возвращаем идентификатор роли
            return role_obj.id
        else:
            # Возвращаем None, если роль не найдена
            return None