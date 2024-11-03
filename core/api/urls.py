from django.urls import path, include


urlpatterns = [
    path('events/', include('events.urls')),
    path('reg/', include('registration.urls')),
]