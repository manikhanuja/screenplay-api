from rest_framework import serializers
from api.models import Screenplay

class ScreenplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenplay
        fields = ('id', 'title', 'genre', 'year', 'writer', 'country', 'language', 'poster_url', 'script_url', 'imdb_rating', 'rotten_tomato_rating')