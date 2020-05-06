# from django.db import models
#
# # Create your models here.
#
#
# class Location(models.Model):
#     name = models.CharField(max_length=50)
#
#     class Meta:
#         verbose_name = "Location"
#         verbose_name_plural = "Locations"
#
#     def __str__(self):
#         return self.name
#
# class Gym(models.Model):
#     name = models.CharField(max_length=50)
#     price = models.IntegerField(default=0)
#     # location = models.ForeignKey(Location, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = "Gym"
#         verbose_name_plural = "Gyms"
#
#     def __str__(self):
#         return self.name
#
#

from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name

class Gym(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    review = models.TextField(blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location')

    def __str__(self):
        return self.name