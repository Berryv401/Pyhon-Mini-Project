from django.contrib import admin
from apps.api.models import Gym
from apps.api.models import Location

# Register your models here.
admin.site.register(Gym)
admin.site.register(Location)