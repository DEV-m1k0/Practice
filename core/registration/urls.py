from django.urls import path
from . import views


"""

# SECTION - ===================== Маршрутизация приложения =====================

Данный файл используется для маршрутизации приложения и отвечает за
маршрутизацию ссылок, которые отвечают за регистрацию пользователей.

Более подробно вы можете ознакомиться в документации Django
https://docs.djangoproject.com/en/4.2/topics/http/urls/

"""


urlpatterns = [
    path('management', views.UserRegistrationAPIView.as_view(), name="reg_management"),
    path('management/import', views.UsersImportExcel.as_view(), name="users_import"),
]



"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""