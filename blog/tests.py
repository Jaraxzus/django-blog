from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Post
from .serializers import PostSerializer


class PostViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.post_data = {
            "title": "Test Post",
            "content": "This is a test post.",
            "author": "John Doe",
        }
        self.post = Post.objects.create(
            title="Existing Post",
            content="Existing content",
            author="Jane Doe",
        )

    def test_list_posts(self):
        url = reverse("post-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_post(self):
        url = reverse("post-list")
        response = self.client.post(url, data=self.post_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(), 2)

    def test_delete_post(self):
        url = reverse("post-detail", args=[self.post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Post.objects.count(), 0)
