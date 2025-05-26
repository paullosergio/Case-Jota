import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from users.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_user():
    return User.objects.create_user(username="testuser", email="test@example.com", password="testpass123")


@pytest.fixture
def admin_user():
    return User.objects.create_user(
        username="admin", email="test@example.com", password="admin123", is_staff=True, role="admin"
    )


@pytest.mark.django_db
class TestUserAPI:
    def test_user_registration(self, api_client):
        url = reverse("register")
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpass123",
            "password2": "newpass123",
        }
        response = api_client.post(url, data)
        print(response.json())
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(username="newuser").exists()

    def test_user_login(self, api_client, test_user):
        url = reverse("token_obtain_pair")
        data = {"username": "testuser", "password": "testpass123"}
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data
        assert "refresh" in response.data

    def test_user_profile(self, api_client, admin_user):
        api_client.force_authenticate(user=admin_user)
        url = reverse("admin-users-list")
        response = api_client.get(url)
        print(response.json())
        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]["username"] == "admin"
        assert response.data[0]["email"] == "test@example.com"

    def test_update_user_profile(self, api_client, admin_user):
        api_client.force_authenticate(user=admin_user)
        url = reverse("admin-users-detail", kwargs={"pk": admin_user.id})
        data = {"username": "updateduser", "email": "updated@example.com", "password": "admin123"}
        response = api_client.put(url, data)
        print(response.json())
        assert response.status_code == status.HTTP_200_OK
        admin_user.refresh_from_db()
        assert admin_user.username == "updateduser"
        assert admin_user.email == "updated@example.com"

    def test_unauthorized_profile_access(self, api_client):
        url = reverse("admin-users-list")
        response = api_client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
