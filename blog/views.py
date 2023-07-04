from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Post
from .serializers import PostSerializer
from .permissoins import IsOwnerOrReadOnly

from django.contrib.auth.models import User


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# class PostAPIList(generics.ListAPIView):
#     queryset = Post.published.all()
#     serializer_class = PostSerializer
#
#
# class PostAPIrud(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostAPICreate(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#

# class PostsAPIView(APIView):
#     def get(self, request):
#         lst = Post.published.all().values()
#         return Response({"posts": list(lst)})
#
#     def post(self, request):
#         # нужно проверит регистрацию, и принадлежность поста к пользователю
#         if "id" in request.data:
#             update_post(request.data)
#         post = post_create_or_update(data=request.data)
#         return Response({"post": PostSerializer(post).data})
#
#     def delete(self, request, *args, **kwargs):
#         if "id" not in kwargs:
#             return Response({"errors": "Menthod DELETE not allowed"})
#         post = Post.objects.get(id=kwargs["id"])
#         post.delete()
#         return Response({"post": f"delete post with id {kwargs['id']}"})
#
#
# def post_create_or_update(*args, **kwargs):
#     serializer = PostSerializer(*args, **kwargs)
#     serializer.is_valid(raise_exception=True)
#     post = serializer.save()
#     return post
#
#
# def update_post(data):
#     try:
#         post = Post.objects.get(id=data["id"])
#     except Post.DoesNotExist:
#         raise ValidationError("Post not found")
#     post = post_create_or_update(post, data=data)
#     return Response({"updated_post": PostSerializer(post).data})
#

# class PostsAPIView(generics.ListAPIView):
#     queryset = Post.published.all()
#     serializer_class = PostSerializer
