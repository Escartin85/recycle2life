# django imports
from django.db import models
# third party imports

# APP imports


class Image(models.Model):
    name_img = models.CharField(max_length=45)
    format_img = models.CharField(max_length=4)
    title_img = models.CharField(max_length=45)
    path_img = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name_img
