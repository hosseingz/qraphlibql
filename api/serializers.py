from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }
    
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise ValidationError("This username is already taken.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("This email is already registered.")
        return value

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise AuthenticationFailed("Invalid username or password.")
        
        return {
            'user': user,
            'message': 'Login successful!',
        }



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death']
    
    def validate_first_name(self, value):
        if not value:
            raise ValidationError("First name cannot be empty.")
        return value

    def validate_last_name(self, value):
        if not value:
            raise ValidationError("Last name cannot be empty.")
        return value


    def create(self, validated_data):
        author, _ = Author.objects.get_or_create(**validated_data)
        return author



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

    def validate_name(self, value):
        if not value:
            raise ValidationError("name cannot be empty.")
        return value


    def create(self, validated_data):
        genre, _ = Genre.objects.get_or_create(**validated_data)
        return genre



class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer(many=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'summary', 'genre', 'published_date', 'page_count', 'cover_image']
    
   
