from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marvel.api.urls', namespace='api-marvel')),
    # path(f'{BASE_URL}/', include(router.urls)),
]
