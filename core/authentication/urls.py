from django.urls import path
from . import views


urlpatterns = [
    path('', views.AuthenticationAPIView.as_view(), name='auth'),
    path('me', views.AccounMeAPIView.as_view())
]