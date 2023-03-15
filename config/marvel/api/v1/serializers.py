from marvel.models import ComicBook
from rest_framework import serializers


class ComicBookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=300, read_only=True)

    def create(self, validated_data):
        return ComicBook.objects.create(**validated_data)
