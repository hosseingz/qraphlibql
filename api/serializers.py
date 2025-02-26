from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

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
        if user:
            return user
        raise serializers.ValidationError('Invalid credentials')





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
        fields = ['id', 'title', 'author', 'summary', 'genre', 'published_date', 'page_count']

    def validate_title(self, value):
        if not value:
            raise ValidationError("Title cannot be empty.")
        return value

    def validate_summary(self, value):
        if not value:
            raise ValidationError("Summary cannot be empty.")
        if len(value) > 1024:
            raise ValidationError("Summary cannot exceed 1024 characters.")
        return value

    def validate_page_count(self, value):
        if value is not None and value <= 0:
            raise ValidationError("Page count must be a positive integer.")
        return value

    def create(self, validated_data):
        author_data = validated_data.pop('author', None)
        genre_data = validated_data.pop('genre', None)

        if not author_data:
            raise ValidationError('Author must be provided.')
        
        author, _ = Author.objects.get_or_create(**author_data)
        book = Book.objects.create(author=author, **validated_data)
            
        if genre_data:
            for genre in genre_data:
                genre_instance, _ = Genre.objects.get_or_create(**genre)
                book.genre.add(genre_instance)

        book.save()

        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)
        genre_data = validated_data.pop('genre', None)

        if author_data:
            author, _ = Author.objects.get_or_create(**author_data)
            instance.author = author
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if genre_data:
            instance.genre.clear()
            for genre in genre_data:
                genre_instance, _ = Genre.objects.get_or_create(**genre)
                instance.genre.add(genre_instance)

        instance.save()
        return instance
