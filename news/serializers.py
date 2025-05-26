from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source="author.username", read_only=True)
    vertical_name = serializers.CharField(source="vertical.name", read_only=True)

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "subtitle",
            "image",
            "content",
            "publish_at",
            "created_at",
            "updated_at",
            "author",
            "author_username",
            "status",
            "vertical",
            "vertical_name",
            "is_pro_only",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "author",
            "author_username",
            "vertical_name",
        ]
