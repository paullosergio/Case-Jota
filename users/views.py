from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView

from .permissions import IsAdmin
from .serializers import CustomTokenObtainPairSerializer, UserSerializer

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserAdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
