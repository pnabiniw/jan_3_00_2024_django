from django.contrib.auth.models import User

from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, \
    UpdateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from crud.models import ClassRoom, UserProfile

from .serializers import ClassRoomModelSerializer, UserProfileModelSerializer, UserSerializer
from .permissions import CheckObjectLevelPermission, IsSuperAdminUser


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

    def get_permissions(self):
        method = self.request.method.lower()
        print(method)
        if method in ["delete", "put", "patch", "post"]:
            print("Permission Super User")
            return [IsSuperAdminUser()]
        print("Permission Allow Any")
        return [AllowAny()]

# delete, put, patch, post => superadmin
# get => AllowAny


class UserProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["address", "user__first_name", "user__last_name"]
    filterset_fields = ["user__is_active"]
    serializer_class = UserProfileModelSerializer
    queryset = UserProfile.objects.all()

    def list(self, *args, **kwargs):
        qp = self.request.query_params
        params = self.request.GET
        print(params)
        print(qp)
        return super().list(*args, **kwargs)


class UserViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        method = self.request.method.lower()
        print(method)
        if method == ['delete', "post"]:
            print("permission superadmin")
            return [IsSuperAdminUser(), ]
        if method in ['put', 'patch']:
            print("permisiion object level")
            return [IsAuthenticated(), CheckObjectLevelPermission()]
        print("permission all")
        return [AllowAny(), ]

    # def get_queryset(self):
    #     user = self.request.user  # user object
    #     method = self.request.method.lower()
    #     if method in ['put', 'patch']:  # This is update
    #         return User.objects.filter(id=user.id)
    #     return User.objects.all()
