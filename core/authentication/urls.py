from django.urls import path
from . import views


"""

# SECTION - ===================== Маршрутизация приложения =====================

Данный файл используется для маршрутизации приложения и отвечает за
маршрутизацию ссылока, которые отвечают за работу с пользователями.

Более подробно вы можете ознакомиться в документации Django
https://docs.djangoproject.com/en/4.2/topics/http/urls/

"""


urlpatterns = [
    path('', views.AuthenticationAPIView.as_view(), name='auth'),
    path('me', views.AccounMeAPIView.as_view())
]


"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""