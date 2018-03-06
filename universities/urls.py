from django.urls import path

from .views import UniversitiesListAPIView


urlpatterns = [
    path(r'', UniversitiesListAPIView.as_view(), name='universities-list')
]
