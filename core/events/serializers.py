from rest_framework import serializers
from models.models import Event, User
from sqlalchemy import select
from models.config import session


"""

# SECTION - ===================== Сериализаторы для событий =====================

Данный файл используется для создания сериализаторов.

"""


class EventSerializer(serializers.Serializer):
    """
    Сериализатор для мероприятий
    """
    # Поле для названия события
    title = serializers.CharField(max_length=255)
    # Поле для изображения события
    photo = serializers.ImageField()
    # Поле для даты события
    date = serializers.DateField()
    # Поле для выбора пользователей
    user = serializers.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Создаем sql запрос для получения всех пользователей
        users_sql = select(User)
        # Выполняем sql запрос и получаем список пользователей
        users = session.scalars(users_sql)
        # Присваиваем полученный список пользователей в поле choices сериализатора
        self.fields['user'].choices = users

class EventExcelSerializers(serializers.Serializer):
    """
    Сериализатор для экселя мероприятий
    """
    excel = serializers.FileField()