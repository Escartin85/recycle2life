# django imports
from django.db import models
# third party imports

# APP imports


class Image(models.Model):
    title = models.CharField(max_length=255)
    format = models.CharField(max_length=4)
    file = models.FileField(upload_to='uploads/images/ads', max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
