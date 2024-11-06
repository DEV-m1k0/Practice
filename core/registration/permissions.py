from rest_framework.permissions import BasePermission
from models.config import session
from sqlalchemy import select
from models.models import Role, User
from rest_framework.request import HttpRequest


"""

#SECTION - ================ Файл для создания кастомных разрешений ================

В данном файле реализован кастомный класс, который проверяет пользователя,
есть ли у него роль организатора или нет.

Более подробно о работе с правами доступа вы можете ознакомиться в
документации Django REST Framework:
https://www.django-rest-framework.org/api-guide/permissions/

"""


class IsOrganizer(BasePermission):
    """
    Класс для проверки, есть ли у пользователя роль организатора
    """

    def has_permission(self, request: HttpRequest, view):
        """
        Метод проверяет, есть ли у пользователя роль организатора
        """

        # Получаем id текущего пользователя из сессии
        user_id = request.session.get('user_id')

        # Формируем sql запрос
        auth_user_sql = select(User).where(User.id == user_id)

        # Получаем текущего пользователя
        auth_user = session.scalar(auth_user_sql)

        # Формируем sql запрос для получения роли
        role_sql = select(Role).where(Role.name == 'организатор')

        # Получаем роль
        role = session.scalar(role_sql)

        # Проверяем, является ли роль текущего пользователя 'организатор'
        # Если роль 'организатор' существует, возвращаем True
        if auth_user.role_id == role.id:
            return True

        # Если роль 'организатор' не существует, возвращаем False
        return False