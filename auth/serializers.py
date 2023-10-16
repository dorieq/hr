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

