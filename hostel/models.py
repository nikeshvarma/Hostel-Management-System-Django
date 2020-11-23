from django.db import models
from django.contrib.auth.models import User


# Create your models here

class Hostel(models.Model):
    hostel_name = models.CharField(max_length=20)

    def __str__(self):
        return self.hostel_name


class Room(models.Model):
    room_id = models.CharField(max_length=20)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    capacity = models.IntegerField(default=1)

    def __str__(self):
        return self.room_id

