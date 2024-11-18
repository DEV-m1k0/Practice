from django.urls import path, include


"""

# SECTION - ===================== Маршрутизация приложения =====================

Данный файл используется для маршрутизации всего нашего приложения.

Более подробно вы можете ознакомиться в документации Django
https://docs.djangoproject.com/en/4.2/topics/http/urls/

"""


urlpatterns = [
    path('api/', include('api.urls'))
]


"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""