from django.urls import include, path
from rest_framework import routers

from blog.views import *

router = routers.SimpleRouter()
router.register(r"post", PostViewSet)
app_name = "blog"
urlpatterns = [
    path("", include(router.urls)),
    # path("api/v1/postlist/", PostAPIList.as_view()),
    # path("api/v1/create-post/", PostAPICreate.as_view()),
    # path("api/v1/post/<int:pk>", PostAPIrud.as_view())
    # path("api/v1/postlist/<int:id>", views.PostsAPIView.as_view()),
]
