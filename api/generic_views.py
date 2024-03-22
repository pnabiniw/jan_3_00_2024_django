from django.contrib.auth.models import User

from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, \
    UpdateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from crud.models import ClassRoom, UserProfile

from .serializers import ClassRoomModelSerializer, UserProfileModelSerializer, UserSerializer


# GET => retrieve / list
# POST  => create
# PATCH  => partial_update
# PUT  => update
# DELETE  => destroy


# ListCreateAPIView
# RetrieveUpdateDestroyAPIView


# ListUpdateAPIView
# RetrieveCreateAPIView


class ClassRoomGenericView(ListAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()


class ClassRoomGenericCreateView(CreateAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()


class ClassRoomListCreateView(ListCreateAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()


class ClassRoomUpdateView(UpdateAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()


class ClassRoomRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()


class ClassRoomViewSet(ModelViewSet):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileModelSerializer
    queryset = UserProfile.objects.all()


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer
    queryset = User.objects.all()
