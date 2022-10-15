from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('musicapp/', include('musicapp.urls')),
    path('admin/', admin.site.urls),
]
