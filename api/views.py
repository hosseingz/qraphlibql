from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from django.contrib.auth import login
from django.shortcuts import get_object_or_404

from .serializers import UserLoginSerializer  
from .serializers import *



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
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]


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

    
    
class GenreCreateAPIView(generics.CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Genre.objects.all() 
    serializer_class = GenreSerializer
    
    
class GenreUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id'
   
    
class GenreDestroyAPIView(generics.DestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id'
    
class GenresListAPIView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    
class GenreDetailByIdAPIView(generics.RetrieveAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id'
    
    
class BookCreateAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        
        author_data = request.data.pop('author')
        genres_data = request.data.pop('genre')

        author, _ = Author.objects.get_or_create(**author_data)
        
        book = Book.objects.create(author=author, **request.data)
        
        for data in genres_data:
            genre, _ = Genre.objects.get_or_create(**data)
            book.genre.add(genre)

        return Response(BookSerializer(book).data, status=status.HTTP_200_OK)
    
    
    
class BookUpdateAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def put(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        book = Book.objects.get(id=book_id)

       
        author_data = request.data.pop('author', None)
        if author_data:
            author, _ = Author.objects.get_or_create(**author_data)
            book.author = author
        
        
        genres_data = request.data.pop('genre', [])
        book.genre.clear() 
        for data in genres_data:
            genre, _ = Genre.objects.get_or_create(**data)
            book.genre.add(genre)


        for attr, value in request.data.items():
            setattr(book, attr, value)
            
        book.save()

        return Response(BookSerializer(book).data, status=status.HTTP_200_OK)
    
    
class BookDestroyAPIView(generics.DestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    
class BooksListAPIView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookDetailByIdAPIView(generics.RetrieveAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'