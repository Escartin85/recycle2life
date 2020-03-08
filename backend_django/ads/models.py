from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.conf import settings

User = get_user_model()


class Ad(models.Model):
    # User using Foreign Key
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=1500)
    priority = models.CharField(max_length=10)
    location_country = models.CharField(max_length=50)
    location_city = models.CharField(max_length=50)
    location_postcode = models.CharField(max_length=10)
    typeAd = models.CharField(max_length=10)
    external = models.BooleanField(default=False)
    external_link = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_external = models.DateTimeField(blank=True, null=True)
    likes = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)], default=0, blank=True)

    # categories =
    # tags =
    # images =

    def __str__(self):
        return self.title
