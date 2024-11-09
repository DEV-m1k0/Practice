from rest_framework.generics import CreateAPIView
from rest_framework.request import HttpRequest
from .serializers import (UserRegistrationSerializer,
                          UserImportExcelSerializer)
from rest_framework.response import Response
from logic.utils import (generate, validate,
                         image, parse)
from logic.role.find import GetRole
from logic.direction.find import GetDirection
from logic.user.create import CreateUser
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.hashers import make_password
from . import permissions
from sqlalchemy.sql import select
from models.models import User, Event
from models.config import session
from sqlalchemy.types import NULLTYPE


"""

#SECTION - ===================== Файл для создание APIView =====================

В данном файле находятся классы представления, которые используются для рендера
API на страницах.

Более подробно о классах представления вы можете узнать в документации Django:
https://docs.djangoproject.com/en/4.2/topics/http/views/

Более подробно о классах предстваления в Django Rest Framework:
https://www.django-rest-framework.org/api-guide/views/


# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

Исходный код данного проекта станет доступен после окончания практики!

"""


class UsersImportExcel(CreateAPIView):
    """
    Класс для добавления пользователей через excel
    """
    serializer_class = UserImportExcelSerializer
    # permission_classes = (permissions.IsOrganizer,)

    def get_queryset(self):
        """
        Получаем queryset
        """
        try:
            # Формируем запрос в бд
            users_sql = select(User)
            # Получаем данные из бд по запросу
            queryset = session.scalars(users_sql)
        except:
            # Если таблицы еще не созданы, то возвращаем пустой queryset
            queryset = []
        return queryset
    
    def create(self, request: HttpRequest, *args, **kwargs):
        # Достаем данные из request
        excel_file: InMemoryUploadedFile = request.FILES['file']
        # Парсим данные и получаем пользователей и их картинки
        parsed = parse.parse_excel(excel_file)

        if parsed == "BAD_REQUEST":
            return Response({"info": "Пользователи не были добавлены"}, status=400)

        for user in parsed:
            id_number = user["id_number"]
            id_number = user["id_number"]
            username = user["username"]
            password = user["password"]
            first_name = user["first_name"]
            last_name = user["last_name"]
            role = user["role"]
            gender = user["gender"]
            email = user["email"]
            phone = user["phone"]
            direction = user["direction"]
            event = user["event"]
            photo = user["photo"]

            get_role = GetRole(name=role.lower())
            role_id = get_role.get()

            get_direction = GetDirection(name=direction)
            direction_id = get_direction.get()

            event_sql = select(Event).where(Event.title == event)
            events = session.scalars(event_sql)

            try:
                event_id = events.one().id
            except:
                event_id = NULLTYPE

            print(id_number)

            user_create = CreateUser(id_number, username, password,
                                     role_id, gender, first_name,
                                     last_name, photo, email,
                                     phone, direction_id, event_id)
            info, code = user_create.create()


        return Response({"info": info}, status=code)


class UserRegistrationAPIView(CreateAPIView):
    """
    Это API представление позволяет зарегистрировать нового пользователя.
    """

    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.IsOrganizer,)

    def get_queryset(self):
        """
        Получаем список всех пользователей
        """
        users_sql = select(User)
        users = session.scalars(users_sql)
        return users

    def create(self, request, *args, **kwargs):
        """
        Метод для создания нового пользователя
        """

        # Создаем словарь для возврата информации о добавлении пользователя
        response = {}

        # Получаем данные из запроса
        id_number = generate.unique_id_number()
        full_name = request.POST.get('full_name')
        gender = request.POST.get('gender')
        role = request.POST.get('role')
        email = request.POST.get('email')
        phone: InMemoryUploadedFile = request.POST.get('phone')
        direction = request.POST.get('direction')
        event = request.POST.get('event')
        photo = request.FILES.get('photo')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Получаем id роли по ее названию
        get_role = GetRole(name=role)
        role_id = get_role.get()

        # Получаем id направления по его названию
        get_direction = GetDirection(name=direction)
        direction_id = get_direction.get()

        bphoto = image.load_image(photo)

        # Проверяем валидность пароля
        password_is_valid, password_info = validate.password_is_valid(password)
        if not password_is_valid:
            response["info"] = password_info
            return Response(response, status=400)
        
        hash_password = make_password(password)
        
        # Проверяем валидность полного имени
        fullname_is_valid, fullname_info = validate.fullname_is_valid(full_name)
        if not fullname_is_valid:
            response["info"] = fullname_info
            return Response(response, status=400)
        # Получаем firstname и lastname из full_name
        lastname, firstname = full_name.split(' ')

        # Проверяем валидность email
        email_is_valid, email_info = validate.email_is_valid(email)
        if not email_is_valid:
            response["info"] = email_info
            return Response(response, status=400)

        # Проверяем валидность телефона
        phone_is_valid, phone_info = validate.phone_is_valid(phone)
        if not phone_is_valid:
            response["info"] = phone_info
            return Response(response, status=400)
        
        event_sql = select(Event).where(Event.title == event)
        events = session.scalars(event_sql)

        if events: event_id = events.one().id
        else: event_id = NULLTYPE
        
        # Выполняем создание пользователя
        creation_user = CreateUser(id_number, username,
                                   hash_password, role_id,
                                   gender, firstname,
                                   lastname, bphoto,
                                   email, phone, direction_id,
                                   event_id)
        response["info"], code = creation_user.create()

        return Response(response, code)
    



"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""