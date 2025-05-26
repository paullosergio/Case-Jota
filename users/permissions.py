from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Permite acesso apenas a usuários com role 'admin'
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "admin"


class IsEditor(BasePermission):
    """
    Permite acesso apenas a usuários com role 'editor'
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "editor"


class IsReader(BasePermission):
    """
    Permite acesso apenas a usuários com role 'reader'
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "reader"


class IsAuthorOrAdmin(BasePermission):
    """
    Permite que editores editem apenas suas próprias notícias,
    e admins editem qualquer uma.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.role == "admin":
            return True
        elif request.user.role == "editor":
            return obj.author == request.user
        return False


class IsEditorOrAdmin(BasePermission):
    """
    Permite acesso a usuários com role 'editor' ou 'admin'
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ["editor", "admin"]
