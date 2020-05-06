from apps.api.models import Gym, Location
from apps.api.serializers import GymSerializer, LocationSerializer
from rest_framework import generics

class GymListCreateView(generics.ListCreateAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer

    def perform_create(self, serializer):
        serializer.save()

class GymDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gym.objects.all()
    serializer_class = LocationSerializer

class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        serializer.save()

class LocationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer




er_class = GymSerializer