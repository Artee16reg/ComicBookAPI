from django.urls import path, include

from marvel.apps import MarvelConfig

app_name = MarvelConfig.name

urlpatterns = [
    path('v1/', include('marvel.api.v1.urls', namespace='v1'))
]