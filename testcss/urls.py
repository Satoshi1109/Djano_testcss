from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cssapp/', include('cssapp.urls')),
    path('admin/', admin.site.urls),
]