from django.urls import path

from .views import home, root_page, temp_inherit_home, portfolio, classroom

urlpatterns = [
    path("home/", home),
    path("portfolio/", portfolio, name="portfolio"),
    path("temp-inherit-home/", temp_inherit_home, name="temp_inherit_home"),
    path('classroom/', classroom, name="classroom"),
    path("", root_page, name="root_page")
]
