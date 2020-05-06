from rest_framework import serializers
from apps.api.models import Gym, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location

        fields = ('id', 'name',)

class GymSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False, read_only=True)
    class Meta:
        model = Gym

        fields = ('id', 'name', 'price', 'description', 'review', 'location',)
