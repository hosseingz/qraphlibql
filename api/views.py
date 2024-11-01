from rest_framework.authentication import BasicAuthentication
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserLoginSerializer  
from rest_framework.views import APIView
from rest_framework import viewsets
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
    
    
    
