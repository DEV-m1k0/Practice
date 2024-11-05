from rest_framework.request import HttpRequest
from rest_framework.permissions import BasePermission


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