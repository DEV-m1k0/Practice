from django.urls import path
from .views import EventsApi, EventbyidApi

urlpatterns = [
    path("", EventsApi.as_view()),
    path('<int:id>/', EventbyidApi.as_view()),
]