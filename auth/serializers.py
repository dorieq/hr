from rest_framework import serializers

class UserRegistrationSerializer(serializers.Serializer):
    itin = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    role = serializers.CharField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    phone = serializers.CharField()
    position = serializers.CharField()


class PositionSerializer(serializers.Serializer):
    # Define the fields for the Position serializer
    name = serializers.CharField()
    description = serializers.CharField()

class LocationSerializer(serializers.Serializer):
    # Define the fields for the Location serializer
    name = serializers.CharField()
    address = serializers.CharField()

class DepartmentSerializer(serializers.Serializer):
    # Define the fields for the Department serializer
    name = serializers.CharField()
    description = serializers.CharField()