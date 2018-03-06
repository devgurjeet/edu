from django.urls import path

from .views import hello
urlpatterns = [
    path(r'', hello, name='hello')
]
