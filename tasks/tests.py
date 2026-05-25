from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task


class TaskApiTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="john",
            password="password123",
        )

        self.assignee = User.objects.create_user(
            username="alex",
            password="password123",
        )

        self.client.force_authenticate(
            user=self.user,
        )

    def test_create_task(self):
        response = self.client.post(
            "/api/tasks/",
            {
                "title": "Build API",
                "description": "Task API",
                "assignee": self.assignee.id,
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            Task.objects.count(),
            1,
        )

    def test_complete_task(self):
        task = Task.objects.create(
            title="Test task",
            creator=self.user,
        )

        response = self.client.post(
            f"/api/tasks/{task.id}/complete/",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        task.refresh_from_db()

        self.assertTrue(task.is_completed)
        self.assertEqual(task.status, "done")

    def test_add_comment(self):
        task = Task.objects.create(
            title="Task with comment",
            creator=self.user,
        )

        response = self.client.post(
            f"/api/tasks/{task.id}/add_comment/",
            {
                "text": "Looks good",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            task.comments.count(),
            1,
        )