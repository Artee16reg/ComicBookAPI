from marvel.models import ComicBook
from rest_framework import serializers


class ComicBookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=300)

    class Meta:
        model = ComicBook
        fields = '__all__'

