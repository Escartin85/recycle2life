# third party imports
from rest_framework import serializers
# APP imports
from ad_categories.models import AdCategory


class AdCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdCategory
        fields = (
            'name_category',
            'date_created',
            'date_updated'
        )
