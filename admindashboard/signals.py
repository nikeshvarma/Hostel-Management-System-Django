from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from hostel.models import Room


@receiver(post_save, sender=User)
def capacity_decrement(sender, instance, allotted, **kwargs):
    if allotted:
        Room.capacity -= 1
