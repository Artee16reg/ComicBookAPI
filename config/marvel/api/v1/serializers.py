from marvel.models import ComicBook
from rest_framework import serializers


class ComicBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComicBook
        fields = '__all__'
