from django.contrib import admin
from django.urls import path, include

# from myapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/', include('crud.urls')),
    path('', include('myapp.urls')),
]
