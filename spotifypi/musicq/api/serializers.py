from rest_framework import serializers
from musicq.models import Song
class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = ('title', 'artist', 'spotify_url', 'queued')
