from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Comment, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment

        fields = (
            "id",
            "author",
            "text",
            "created_at",
        )

        read_only_fields = (
            "author",
            "created_at",
        )


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for task entity.
    """

    creator = UserSerializer(read_only=True)

    assignee = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
    )

    comments = CommentSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Task

        fields = (
            "id",
            "title",
            "description",
            "creator",
            "assignee",
            "status",
            "is_completed",
            "comments",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "creator",
            "created_at",
            "updated_at",
        )
