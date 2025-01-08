from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser, UserHistory

# class EEUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['login', 'password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['login', 'password']

class UserHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = [ 'age', 'height', 'weight', 'gender']
        extra_kwargs = {
            'user_id': {'write_only': True},  # Не отправляем пароль обратно клиенту
            'age': {'write_only': True},  # Не отправляем пароль обратно клиенту
            'height': {'write_only': True},  # Не отправляем пароль обратно клиенту
            'weight': {'write_only': True}, # Не отправляем пароль обратно клиенту
            'gender': {'write_only': True},  # Не отправляем пароль обратно клиенту
            'date': {'write_only': True},  # Не отправляем пароль обратно клиенту
        }

class UserHistoryReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = ['age', 'height', 'weight', 'gender', 'date', 'bmr', 'body_mass_index', 'effectiv_weight', 'protein', 'fats', 'carbohydrates']

class UserHistoryReturnNowSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = ['bmr', 'body_mass_index', 'effectiv_weight', 'protein', 'fats', 'carbohydrates']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Неверное имя пользователя или пароль.")
        return user