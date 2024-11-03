from rest_framework.permissions import BasePermission
from sqlalchemy.orm import Session
from models.config import engine
from sqlalchemy import select
from models.models import Role


"""

#SECTION - ================ Файл для создания кастомных разрешений ================

В данном файле реализован кастомный класс, который проверяет пользователя,
есть ли у него роль организатора или нет.

"""


class IsOrganizer(BasePermission):
    """
    Класс для проверки, есть ли у пользователя роль организатора
    """

    def has_permission(self, request, view):
        """
        Метод проверяет, есть ли у пользователя роль организатора
        """

        # Получаем id текущего пользователя из заголовка запроса
        user_id = request.user.id

        # Получаем роль текущего пользователя из базы данных
        with Session(engine) as session:
            user_role_sql_row = select(Role).where(Role.id == user_id)
            user_role = session.scalar(user_role_sql_row)

        # Если роль текущего пользователя 'организатор', возвращаем True
        if user_role.name == "организатор":
            return True

        # Если роль текущего пользователя не 'организатор', возвращаем False
        return False