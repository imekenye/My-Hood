from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Profile


# Create your models here.
class Post(models.Model):
    post_image = models.ImageField(upload_to='post_pics/')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class NeighbourHood(models.Model):
    hood_name = models.CharField(max_length=50)
    hood_location = models.CharField(max_length=50)
    occupants = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.hood_name


class Business(models.Model):
    business_name = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name='neighborhood', null=True)
    hood_id = models.ForeignKey(NeighbourHood, blank=True, on_delete=models.CASCADE,
                                related_name='neighborhood', null=True)
    business_email = models.EmailField(max_length=70, blank=True)
