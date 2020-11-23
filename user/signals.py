from django.core.mail import send_mail
from .models import *
from django.dispatch import receiver
from django.db.models.signals import post_save


# most important code for connect tables
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if not created:
        instance.profile.save()
# post_save.connect(update_profile, sender=User)
