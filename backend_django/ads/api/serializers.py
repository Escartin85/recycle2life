# third party imports
from rest_framework import serializers
# APP imports
from ads.models import Ad


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = (
            'user',
            'title',
            'description',
            'slug',
            'priority',
            'location_country',
            'location_city',
            'location_postcode',
            'typeAd',
            'external',
            'date_created',
            'date_updated',
            'date_external',
            'likes'
        )
