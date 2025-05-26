from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CustomTokenObtainPairView, RegisterView, UserAdminViewSet

router = DefaultRouter()
router.register(r"admin/users", UserAdminViewSet, basename="admin-users")

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="register"),
] + router.urls
