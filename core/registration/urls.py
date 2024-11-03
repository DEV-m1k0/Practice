from django.urls import path
from . import views


urlpatterns = [
    path('management', views.UserRegistrationAPIView.as_view(), name="reg_management")
]