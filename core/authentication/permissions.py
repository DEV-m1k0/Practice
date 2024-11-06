from rest_framework.request import HttpRequest
from rest_framework.permissions import BasePermission


"""


# SECTION - ================ Файл для создания кастомных разрешений ================

Данный файл предназначени для создания разрешений, для доступа к различным
частям приложения.

Более подробно о работе с правами доступа вы можете ознакомиться в
документации Django REST Framework:
https://www.django-rest-framework.org/api-guide/permissions/

"""


class AuthenticatePermission(BasePermission):
    """
    Класс для проверки авторизации пользователей
    """

    def has_permission(self, request: HttpRequest, view):
        """
        Метод проверяет, авторизован ли пользователь
        """
        # Проверяем авторизован ли пользователь
        if request.session.get("user_id"):
            return True
        return False
    


"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""