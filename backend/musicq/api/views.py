from rest_framework.generics import ListAPIView, RetrieveAPIView


from musicq.models import Song
from .serializers import SongSerializer


class SongListView(ListAPIView):
	queryset = Song.objects.all() # maybe restrict to only the queued ones?
	serializer_class = SongSerializer

# class SongDetailView(RetrieveAPIView):
# 	queryset = Song.objects.all() # maybe restrict to only the queued ones?
# 	serializer_class = SongSerializer