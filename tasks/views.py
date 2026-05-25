from rest_framework import permissions, status, viewsets

from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Comment, Task
from .serializers import CommentSerializer, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        return Task.objects.filter(
            creator=user,
        ) | Task.objects.filter(
            assignee=user,
        )

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @action(detail=True, methods=["post"])
    def complete(self, request, pk=None):
        task = self.get_object()

        task.is_completed = True
        task.status = "done"

        task.save()

        serializer = self.get_serializer(task)

        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def add_comment(self, request, pk=None):
        task = self.get_object()

        serializer = CommentSerializer(
            data=request.data,
        )

        serializer.is_valid(raise_exception=True)

        serializer.save(
            task=task,
            author=request.user,
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(
            author=self.request.user,
        )
