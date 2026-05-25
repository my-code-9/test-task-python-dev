from rest_framework.routers import DefaultRouter

from .views import (
    CommentViewSet,
    TaskViewSet,
)

router = DefaultRouter()

router.register(
    "tasks",
    TaskViewSet,
    basename="tasks",
)

router.register(
    "comments",
    CommentViewSet,
    basename="comments",
)

urlpatterns = router.urls