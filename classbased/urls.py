from django.urls import path
from .views import PortfolioView, ClassRoomView, ClassRoomCreateView


urlpatterns = [
    path('portfolio/', PortfolioView.as_view(), name="classbased_portfolio"),
    path("classroom/", ClassRoomView.as_view(), name="classbased_classroom"),
    path("add-classroom/", ClassRoomCreateView.as_view(), name="classbased_add_classroom")
]
