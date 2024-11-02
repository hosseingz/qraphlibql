from rest_framework.authentication import BasicAuthentication
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserLoginSerializer  
from rest_framework.views import APIView
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

        user = serializer.validated_data['user']

        return Response({
            'username': user.username,
            'message': 'Login successful!',
        }, status=status.HTTP_200_OK)



class AuthorCreateAPIView(generics.CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    
class AuthorUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'
   
    
class AuthorDestroyAPIView(generics.DestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'


class AuthorsListAPIView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    
class AuthorDetailByIdAPIView(generics.RetrieveAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'
    
    
    
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