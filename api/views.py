from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from django.contrib.auth import login
from django.shortcuts import get_object_or_404

from .serializers import UserLoginSerializer  
from .serializers import *
from .permissions import IsAdminOrAllowAny


class SignupAPIView(generics.CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    
    serializer_class = UserRegistrationSerializer


class UserLoginAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        login(request, user=user)

        return Response({
            'username': user.username,
            'message': 'Login successful!',
        }, status=status.HTTP_200_OK)




class AuthorAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminOrAllowAny]


    def get(self, request, id=None, format=None):
        if id:
            author = get_object_or_404(Author, id=id)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        else:
            authors = Author.objects.all()
            serializer = AuthorSerializer(authors, many=True)
            return Response(serializer.data)


    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        author = get_object_or_404(Author, id=id)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        author = get_object_or_404(Author, id=id)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class GenreAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminOrAllowAny]

    def get(self, request, id=None, format=None):
        if id:
            genre = get_object_or_404(Genre, id=id)
            serializer = GenreSerializer(genre)
            return Response(serializer.data)
        else:
            genres = Genre.objects.all()
            serializer = GenreSerializer(genres, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        genre = get_object_or_404(Genre, id=id)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        genre = get_object_or_404(Genre, id=id)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class BookAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminOrAllowAny]

    def get(self, request, id=None, format=None):
        if id:
            book = get_object_or_404(Book, id=id)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        else:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        book = get_object_or_404(Book, id=id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        book = get_object_or_404(Book, id=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        