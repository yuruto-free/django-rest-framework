from django.contrib.auth import password_validation
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['viewname']
        read_only_fields = ['viewname']

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'viewname', 'password']
        read_only_fields = ['username', 'email']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, password):
        if not password_validation.validate_password(password):
            raise serializers.ValidationError(f'The password {password} is not valid')
        
        return password

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)

        try:
            user.set_password(validated_data['password'])
            user.save()
        except Exception:
            pass

        return user
