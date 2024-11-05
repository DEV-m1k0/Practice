from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import UserSerializer
from models.models import User, Role, Direction
from models.config import session
from sqlalchemy.sql import select
from rest_framework.request import HttpRequest
from .permissions import AuthenticatePermission
from datetime import timedelta


# Create your views here.



class AuthenticationAPIView(CreateAPIView):
    """
    Класс для авторизации в систему
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Получаем список пользователей
        """
        users_sql = select(User)
        users = session.scalars(users_sql)
        return users
    
    def create(self, request: HttpRequest, *args, **kwargs):
        # Получаем id_number
        id_number = request.POST.get("id_number")
        # Получаем пароль
        password = request.POST.get("password")

        # Создаем sql запрос
        user_sql = select(User).where(User.id_number == id_number)
        # Используем сессию для выполнения запроса и получения данных
        user = session.scalar(user_sql)

        # Проверяем, есть ли такой пользователь и пароль совпадает
        if user and user.check_user_password(password):
            # Сохраняем id пользователя в сессии и делаем его активным на 1 день
            request.session["user_id"] = user.id
            request.session.set_expiry(timedelta(days=1))
            return Response({f"{user.username}": "Успешно вошел!"}, status=200)

        return Response({"info": "Такого пользователя нет"}, status=400)
    

class AccounMeAPIView(ListAPIView):
    """
    Класс для получения информации о текущем пользователе
    """
    serializer_class = UserSerializer
    permission_classes = [AuthenticatePermission]

    def get_queryset(self):
        """
        Получаем список пользователей
        """
        users_sql = select(User)
        users = session.scalars(users_sql)
        return users
    
    def list(self, request: HttpRequest, *args, **kwargs):
        # Получаем id текущего пользователя из сессии
        user_id = request.session.get("user_id")
        # Получаем информацию о текущем пользователе
        user_sql = select(User).where(User.id == user_id)
        user = session.scalar(user_sql)
        # Создаем словарь с информацией о текущем пользователе
        response = {
                "Никнейм": f"{user.username}",
                "имя": f"{user.firstname}",
                "фамилия": f"{user.lastname}",
                "Почта": f"{user.email}",
                "пол": f"{user.gender}",
                "Номер телефона": f"{user.phone}",
        }
        # Проверяем роль пользователя
        if user.role_id:
            # Получаем название роли текущего пользователя
            role_sql = select(Role).where(Role.id == user.role_id)
            role = session.scalar(role_sql)
            response["Роль"] = f"{role.name}"
        # Проверяем направление пользователя
        if user.direction_id:
            # Получаем название направления текущего пользователя
            direction_sql = select(Direction).where(Direction.id == user.direction_id)
            direction = session.scalar(direction_sql)
            response["Направление"] = f"{direction.name}"
        # Возвращаем информацию о текущем пользователе
        return Response({
            "Информация о пользователе": response
            })