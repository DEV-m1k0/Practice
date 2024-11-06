from rest_framework import serializers


"""

# SECTION - ==================== Сериализаторы для пользователей ====================

Данный файл используется для создания сериализаторов, которые отвечают за
сериализацию и десериализацию данных пользователей.

Более подробно про сериализаторы вы можете ознакомиться в документации 
Django REST Framework:
https://www.django-rest-framework.org/api-guide/serializers/

"""


class UserSerializer(serializers.Serializer):
    """
    Сериализатор для пользователей
    """
    # Поле для идентификатора пользователея, по которуму он будет входить в систему
    id_number = serializers.IntegerField()
    # Поле для ввода пороля
    password = serializers.CharField(max_length=100)


"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""