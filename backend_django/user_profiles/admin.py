# django imports
from django.contrib import admin
# APP imports
from . import models

admin.site.register(models.UserProfile)