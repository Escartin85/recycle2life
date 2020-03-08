# third party imports
from rest_framework import serializers
# APP imports
from images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'name_img',
            'format_img',
            'title_img',
            'path_img',
            'date_created',
            'date_updated'
        )


