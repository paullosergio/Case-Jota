import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from news.models import News
from users.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_user():
    return User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="testpass123",
        role="editor",  # Adicionando role para permitir criação de notícias
    )


@pytest.fixture
def authenticated_client(api_client, test_user):
    api_client.force_authenticate(user=test_user)
    return api_client


@pytest.fixture
def test_news(test_user):
    return News.objects.create(
        title="Test News",
        content="Test Content",
        author=test_user,
        status="published",  # Adicionando status para permitir visualização
    )


@pytest.mark.django_db
class TestNewsAPI:
    def test_create_news(self, authenticated_client):
        url = reverse("news-list")
        data = {
            "title": "New Test News",
            "content": "New Test Content",
            "status": "draft",
            "vertical": "poder",
            "subtitle": "New Test Subtitle",
        }
        response = authenticated_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert News.objects.count() == 1
        assert News.objects.get().title == "New Test News"

    def test_list_news(self, authenticated_client, test_news):
        url = reverse("news-list")
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_retrieve_news(self, authenticated_client, test_news):
        url = reverse("news-detail", kwargs={"pk": test_news.pk})
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == "Test News"

    def test_update_news(self, authenticated_client, test_news):
        url = reverse("news-detail", kwargs={"pk": test_news.pk})
        data = {
            "title": "Updated News",
            "content": "Updated Content",
            "status": "published",
            "vertical": "poder",
            "subtitle": "Updated Subtitle",
        }
        response = authenticated_client.put(url, data)
        print(response.json())
        assert response.status_code == status.HTTP_200_OK
        test_news.refresh_from_db()
        assert test_news.title == "Updated News"

    def test_delete_news(self, authenticated_client, test_news):
        url = reverse("news-detail", kwargs={"pk": test_news.pk})
        response = authenticated_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert News.objects.count() == 0

    def test_unauthorized_access(self, api_client):
        url = reverse("news-list")
        response = api_client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
