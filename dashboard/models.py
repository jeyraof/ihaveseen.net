from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'user_profile'


@receiver(post_save, sender=User, dispatch_uid='create_user')
def generate_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
