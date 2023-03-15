from rest_framework.routers import DefaultRouter

from django.urls import path
from marvel.api.v1.views import comics_list_view, comic_detail_view

app_name = 'v1'

# router = DefaultRouter()
# router.register('marvel/', MarvelViewSet, basename='marvel')
#
# urlpatterns = router.urls
urlpatterns = [
    path('marvel/', comics_list_view),
    path('marvel/<int:pk>/', comic_detail_view),

]
