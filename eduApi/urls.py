from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'uni/', include('universities.urls')),

    # Developer Tools
    path('admin/', admin.site.urls),
]
