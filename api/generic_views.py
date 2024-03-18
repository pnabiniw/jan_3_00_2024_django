from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, \
    UpdateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.viewsets import ModelViewSet
from crud.models import ClassRoom, UserProfile

from .serializers import ClassRoomModelSerializer, UserProfileModelSerializer


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
