from django.db import models
from django.contrib.auth.models import User

from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_email = models.EmailField(max_length=70, blank=True)
    myhood_id = models.ForeignKey('pages.NeighbourHood', blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
