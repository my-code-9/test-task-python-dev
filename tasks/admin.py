from django.contrib import admin

from .models import Comment, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "creator",
        "assignee",
        "status",
        "is_completed",
        "created_at",
    )

    list_filter = (
        "status",
        "is_completed",
    )

    search_fields = (
        "title",
        "description",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "task",
        "author",
        "created_at",
    )

    search_fields = (
        "text",
    )