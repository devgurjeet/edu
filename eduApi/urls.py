from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'universities/', include('universities.urls')),

    # Developer Tools
    path('admin/', admin.site.urls),
]
