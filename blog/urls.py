from django.urls import include, path
from rest_framework import routers

from blog.views import *

router = routers.SimpleRouter()
router.register(r"post", PostViev)
# router.register(r"comment", CommentViev)

app_name = "blog"
urlpatterns = [
    path("", include(router.urls)),
    path("postlist/", PostListView.as_view()),
    # path(
    #     "post/<int:post_id>/comments/",
    #     CommentList.as_view(),
    #     name="comment-list",
    # ),
    path(
        "post/<int:post>/comments/",
        CommentView.as_view({"get": "list", "post": "create"}),
        name="comment-list",
    ),
    path(
        "post/<int:post>/comments/<int:pk>/",
        CommentView.as_view(
            {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
        ),
        name="comment-detail",
    ),
    # path("api/v1/create-post/", PostAPICreate.as_view()),
    # path("api/v1/post/<int:pk>", PostAPIrud.as_view())
    # path("api/v1/postlist/<int:id>", views.PostsAPIView.as_view()),
]
