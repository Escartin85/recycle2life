# third party imports
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer
)
# APP imports
from images.models import Image

## AD IMAGE SERIALIZERS ##
# Serializer for Image LIST
class Image_LIST_Serializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='images-api:detailIMG',
        lookup_field='id'
    )
    class Meta:
        model = Image
        fields = (
            'title',
            'format',
            'file',
            'url',
            'date_created'
            #'date_updated'
        )

# Serializer for Image DETAIL
class Image_DETAIL_Serializer(ModelSerializer):
    url_delete = HyperlinkedIdentityField(
        view_name='images-api:deleteIMG',
        lookup_field='id'
    )
    class Meta:
        model = Image
        fields = (
            'title',
            'format',
            'file',
            'date_created',
            'date_updated',
            'url_delete'
        )

# Serializer for Image CREATE / UPDATE
class Image_CREATEUPDATE_Serializer(ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'title',
            'format',
            'file',
            'date_created',
            'date_updated'
        )
