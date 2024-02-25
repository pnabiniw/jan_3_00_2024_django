from django.urls import path

from .views import home, root_page

urlpatterns = [
    path("home/", home),
    path("", root_page)
]
