from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.permissions import IsAuthorOrAdmin, IsEditorOrAdmin

from .models import News
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
    # Evita erros na geração do schema do Swagger
        if getattr(self, 'swagger_fake_view', False):
            return News.objects.none()

        user = self.request.user

        if user.role == "admin":
            return News.objects.all()

        elif user.role == "editor":
            return News.objects.filter(author=user)

        elif user.role == "reader":
            now = timezone.now()
            qs = News.objects.filter(status="published", publish_at__lte=now)

            plan = user.plan

            if plan == "info":
                return qs.filter(is_pro_only=False)

            elif plan == "pro":
                return qs

        return News.objects.none()

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAuthorOrAdmin()]
        elif self.action == "create":
            return [IsAuthenticated(), IsEditorOrAdmin()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.role == "reader":
            now = timezone.now()
            if instance.status != "published" or instance.publish_at > now:
                return Response({"detail": "Notícia não disponível."}, status=403)

            if instance.is_pro_only:
                if request.user.plan.name != "pro" or instance.vertical not in request.user.verticals.all():
                    return Response(
                        {"detail": "Notícia restrita à vertical do seu plano."},
                        status=403,
                    )

        return super().retrieve(request, *args, **kwargs)
