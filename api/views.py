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
