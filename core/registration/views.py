from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from logic.utils import generate, validate
from logic.role.find import GetRole
from logic.direction.find import GetDirection
from logic.user.create import CreateUser



"""

#SECTION - ===================== Файл для создание APIView =====================

В данном файле находятся классы представления, которые используются для рендера
API на страницах.

"""


class UserRegistrationAPIView(CreateAPIView):
    """
    Это API представление позволяет зарегистрировать нового пользователя.
    """

    serializer_class = UserRegistrationSerializer
    # queryset: list
    # permission_classes = (permissions.IsOrganizer,)

    def create(self, request, *args, **kwargs):
        """
        Метод для создания нового пользователя
        """

        print(request.POST)
        print(request.FILES)

        # Создаем словарь для возврата информации о добавлении пользователя
        response = {}

        # Получаем данные из запроса
        id_number = generate.unique_id_number()
        full_name = request.POST.get('full_name')
        gender = request.POST.get('gender')
        role = request.POST.get('role')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
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

        print(role_id, direction_id)

        #TODO - Доделать регистрацию жюри/модератора. Остановился на момента
        # прикрепления жюри/модератора на мероприятие

        # Проверяем валидность пароля
        password_is_valid, password_info = validate.password_is_valid(password)
        if not password_is_valid:
            response["info"] = password_info
            return Response(response, status=400)
        
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
        
        # Выполняем создание пользователя
        creation_user = CreateUser(id_number, username,
                                   password, role_id,
                                   gender, firstname,
                                   lastname, photo,
                                   email, phone, direction_id)
        response["info"], code = creation_user.create()

        return Response(response, code)

    # def __init__(self, **kwargs) -> None:
    #     super().__init__(**kwargs)
    #     self.queryset = self.set_queryset()

    # def set_queryset(self):
    #     """
    #     Метод для получения доступных клиентам пользователей из базы данных.
    #     """

    #     queryset_sql_row = select(User)
    #     with Session(engine) as session:
    #         queryset = session.scalars(queryset_sql_row)

    #     return queryset