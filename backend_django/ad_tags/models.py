# django imports
from django.db import models
# third party imports

# APP imports


class AdTag(models.Model):
    name_tag = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name_tag
