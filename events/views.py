from events.models import Event
from events.serializers import EventSerializer
from rest_framework import generics


class EventList(generics.ListCreateAPIView):
    """
    List all events, or create a new event.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete an event instance.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
