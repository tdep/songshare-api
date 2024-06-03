from songs.models import Song
from songs.serializers import SongSerializer
from rest_framework import generics


class SongsList(generics.ListCreateAPIView):
    """
    List all songs, or create a new song.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a song instance.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
