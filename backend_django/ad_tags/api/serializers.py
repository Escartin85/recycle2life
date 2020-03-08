# third party imports
from rest_framework import serializers
# APP imports
from ad_tags.models import AdTag


class AdTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdTag
        fields = (
            'name_tag',
            'date_created',
            'date_updated',
        )
