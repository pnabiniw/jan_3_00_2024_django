# Serializers help to serialize and deserialize data
# Process of converting native types (queryset, object) to JSON data is serialization
# Process of validating and converting JSON type to python object is deserialization

from rest_framework import serializers
from crud.models import ClassRoom


class ClassroomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=5)


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', "name"]
