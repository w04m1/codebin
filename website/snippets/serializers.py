from rest_framework import serializers
from .models import Snippet, Comment, Reaction


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        exclude = ("owner",)
        # fields = ""

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().update(instance, validated_data)
