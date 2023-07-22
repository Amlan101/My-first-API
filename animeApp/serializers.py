from rest_framework import serializers
from animeApp.models import AnimeApp


class AnimeAppSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnimeApp
        fields = ('id','name','author','rating','releaseDate')