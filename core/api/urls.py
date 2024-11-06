from django.urls import path, include


"""

# SECTION - ===================== Маршрутизация приложения =====================

Данный файл используется для маршрутизации приложения и отвечает за
маршрутизацию ссылока, которые идут после api/

Более подробно вы можете ознакомиться в документации Django
https://docs.djangoproject.com/en/4.2/topics/http/urls/

"""


urlpatterns = [
    path('events/', include('events.urls')),
    path('reg/', include('registration.urls')),
    path('auth/', include('authentication.urls')),
]


"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""