from rest_framework import serializers
from models.models import GENDERS
from logic.event.find import GetEvent
from sqlalchemy.sql import select
from models.config import session
from models.models import Event


"""

#SECTION - ================== Файл для создания сереализаторов ==================

В данном файле расспологаются классы сериализаторы, которые будут сериализировать
данные приходящии из клиента.

Более подробно про сериализаторы вы можете ознакомиться в документации 
Django REST Framework:
https://www.django-rest-framework.org/api-guide/serializers/

"""

JURY_OR_MODERATOR = ["жюри", "модератор"]


class UserImportExcelSerializer(serializers.Serializer):
    """
    Сериализатор для импорта пользователей из Excel файла
    """
    file = serializers.FileField(help_text="Необходимый формат: .xls, .xlsx")


class UserRegistrationSerializer(serializers.Serializer):
    """
    Сериализатор для регистрации жюри/модераторов
    """

    full_name = serializers.CharField(max_length=255, required=True, help_text="Порядок слов: Фамилия Имя")
    gender = serializers.ChoiceField(GENDERS, required=True)
    role = serializers.ChoiceField(JURY_OR_MODERATOR, required=True)
    email = serializers.EmailField(max_length=255, required=True)
    phone = serializers.CharField(max_length=17, required=True, help_text="Пример: +7(999)-999-99-99")
    direction = serializers.CharField(max_length=255, required=True)
    event = serializers.ChoiceField(choices=[], required=True)
    photo = serializers.ImageField(required=False)
    username = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True)
        
    def __init__(self, *args, **kwargs):
        super(UserRegistrationSerializer, self).__init__(*args, **kwargs)
        events_sql = select(Event)
        events = session.scalars(events_sql)
        self.fields["event"].choices = events



"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""