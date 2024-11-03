from django.urls import path
from .views import EventsApi 

urlpatterns = [
    path("", EventsApi.as_view()),
]