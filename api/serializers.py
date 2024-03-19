# Serializers help to serialize and deserialize data
# Process of converting native types (queryset, object) to JSON data is serialization
# Process of validating and converting JSON type to python object is deserialization
from django.contrib.auth.models import User

from rest_framework import serializers
from crud.models import ClassRoom, UserProfile


class ClassroomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=5)


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', "name"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "is_active", "username", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)  # user creation
        user.set_password(password)  # user password hashed
        user.save()
        return user


class UserProfileModelSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ["id", "address", "phone", "user", "profile_picture"]

    def get_fields(self):
        request = self.context.get("request")
        fields = super().get_fields()
        if request and request.method == "GET":
            fields['user'] = UserSerializer()
        return fields
