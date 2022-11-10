from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        fields = ['email', 'first_name', 'second_name', 'phone_number', 'password', 'password2']
        model = User

    def save(self):
        if not self.validated_data['password'] == self.validated_data['password2']:
            raise serializers.ValidationError({'Error': 'Passwords do not match'})
        
        user = User(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            second_name=self.validated_data['second_name'],
        )
        user.set_password(self.validated_data['password'])
        user.save()
        Token.objects.create(user=user)

        return user

    def update(self, validated_data, instance):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)
        instance.save()

        return instance




