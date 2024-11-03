from base import BaseRole
from models.models import Role
from sqlalchemy.sql import select
from sqlalchemy.orm import Session
from models.config import engine



"""

#SECTION - ======================= Пакет для поиска ролей =======================

"""



class GetRoleId(BaseRole):
    """
    Класс для получения идентификатора роли по имени.
    """
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def get_id_by_role(self):
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