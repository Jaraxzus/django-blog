from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_page
from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import generics

from .models import Comment, Post
from .permissoins import IsOwnerOrReadOnly
from .serializers import CommentSerializer, PostSerializer
from .utils.cache_utils import delete_cache


# from django.contrib.auth.models import User
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.exceptions import ValidationError
class PostListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 30


class PostListView(generics.ListCreateAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = PostListPagination

    CACHE_KEY_PREFIX = "post-list"

    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response


class PostViev(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    # class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    # pagination_class = PostListPagination

    CACHE_KEY_PREFIX = "post-view"

    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response


# class CommentList(generics.ListCreateAPIView):
#     # serializer_class = CommentSerializer
#     # permission_classes = (IsOwnerOrReadOnly,)
#
#     def get_queryset(self):
#         post_id = self.kwargs["post_id"]
#         queryset = Comment.objects.filter(post_id=post_id)
#         return queryset
#


class CommentView(viewsets.ModelViewSet):
    CACHE_KEY_PREFIX = "comments"
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response
