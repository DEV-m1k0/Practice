from django.urls import path
from .views import EventsApi, EventbyidApi, ExcelEvent

urlpatterns = [
    path("", EventsApi.as_view()),
    path('<int:id>/', EventbyidApi.as_view()),
    path('import/', ExcelEvent.as_view())
]