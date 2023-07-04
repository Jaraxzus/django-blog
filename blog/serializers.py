from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = (
            "title",
            "slug",
            "author",
            "body",
            "publish",
            "created",
            "update",
            "status",
        )
        read_only_fields = ["publish", "created", "update"]

    # def create(self, validated_data):
    #     # post_keys_to_keep = ["title", "slug", "author", "body", "status"]
    #     # post_data = {
    #     #     key: validated_data[key]
    #     #     for key in validated_data.keys()
    #     #     - (validated_data.keys() - post_keys_to_keep)
    #     # }
    #
    #     return super().create(validated_data)
