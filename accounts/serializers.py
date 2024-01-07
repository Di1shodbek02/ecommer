from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(style={'input_type': 'confirm_password'}, write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password', 'confirm_password')

    def create(self, validated_date):
        user = User.objects.create_user(
            first_name=validated_date['first_name'],
            last_name=validated_date['last_name'],
            username=validated_date['username'],
            email=validated_date['email'],
            phone_number=validated_date['phone_number'],
            password=validated_date['password'],
        )
        return user
