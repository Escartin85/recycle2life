from django.contrib import admin

from .models import Ad, AdTag, AdCategory

admin.site.register(Ad)
admin.site.register(AdCategory)
admin.site.register(AdTag)