from django.db import models
from django.contrib.auth.models import User


from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_email = models.EmailField(max_length=70, blank=True)
    hood = models.ForeignKey('pages.NeighbourHood', on_delete=models.CASCADE, related_name="profile_hood", null=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
