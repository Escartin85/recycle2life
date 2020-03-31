# django imports
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.urls import reverse
from django.conf import settings

# third party imports

# APP imports
from images.models import Image

User = get_user_model()


class AdCategory(models.Model):
    name_category = models.CharField(max_length=45)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    class Meta:
        ordering = ['name_category']

    def __str__(self):
        return self.name_category
    
    def get_api_url(self):
        return reverse("ads-api:detailCAT", kwargs={"id": self.id})

class AdTag(models.Model):
    name_tag = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    class Meta:
        ordering = ['name_tag']

    def __str__(self):
        return self.name_tag
    
    def get_api_url(self):
        return reverse("ads-api:detailTAG", kwargs={"id": self.id})

class Ad(models.Model):
    OFFERED = 'OF'
    WANTED = 'WA'
    HIGH = '3'
    MEDIUM = '2'
    LOW = '1'
    TYPE_AD_CHOICES = [
        (OFFERED, 'Offered'),
        (WANTED, 'Wanted'),
    ]
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')
    ]
    # User using Foreign Key
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=1500)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=MEDIUM)
    location_country = models.CharField(max_length=50)
    location_city = models.CharField(max_length=50)
    location_postcode = models.CharField(max_length=10)
    typeAd = models.CharField(max_length=10, choices=TYPE_AD_CHOICES, default=OFFERED)
    external = models.BooleanField(default=False, blank=True)
    external_link = models.CharField(max_length=500, blank=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    date_external = models.DateTimeField(blank=True, null=True)
    likes = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)], default=0, blank=True)
    # Relationships
    categories = models.ManyToManyField(AdCategory)
    tags = models.ManyToManyField(AdTag)
    images = models.ManyToManyField(Image)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.title
