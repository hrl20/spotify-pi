from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets, permissions
from musicq.models import Song
from .serializers import SongSerializer


class SongListView(ListAPIView):
	queryset = Song.objects.all() # maybe restrict to only the queued ones?
	serializer_class = SongSerializer

class SongViewSet(viewsets.ModelViewSet):
	queryset = Song.objects.all()
	permission_classes = [
	  permissions.AllowAny
	]
	serializer_class = SongSerializer
# class SongDetailView(RetrieveAPIView):
# 	queryset = Song.objects.all() # maybe restrict to only the queued ones?
# 	serializer_class = SongSerializer