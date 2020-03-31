# third party imports
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer
)
# APP imports
from ads.models import Ad, AdCategory, AdTag

## AD TAG SERIALIZERS ##
# Serializer for Ad Tag LIST
class AdTag_LIST_Serializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='ads-api:detailTAG',
        lookup_field='id'
    )
    class Meta:
        model = AdTag
        fields = [
            #'id',
            'name_tag',
            'url',
            'date_created',
            #'date_updated'
        ]
        #extra_kwargs = {
        #    'url': {'lookup_field': 'id'}
        #}

# Serializer for Ad Tag DETAIL
class AdTag_DETAIL_Serializer(ModelSerializer):
    
    class Meta:
        model = AdTag
        fields = [
            'id',
            'name_tag',
            #'date_created',
            'date_updated'
        ]

# Serializer for Ad Tag CREATE / UPDATE
class AdTag_CREATEUPDATE_Serializer(ModelSerializer):
    
    class Meta:
        model = AdTag
        fields = [
            #'id',
            'name_tag',
            'date_created',
            'date_updated'
        ]

## AD CATEGORY SERIALIZERS ##
# Serializer for Ad Category LIST
class AdCategory_LIST_Serializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='ads-api:detailCAT',
        lookup_field='id'
    )
    class Meta:
        model = AdCategory
        fields = (
            'id',
            'url',
            'name_category',
            'date_created',
            #'date_updated'
        )

# Serializer for Ad Category DETAIL
class AdCategory_DETAIL_Serializer(ModelSerializer):
    class Meta:
        model = AdCategory
        fields = (
            'id',
            'name_category',
            #'date_created',
            'date_updated'
        )

# Serializer for Ad Category CREATE / UPDATE
class AdCategory_CREATEUPDATE_Serializer(ModelSerializer):
    class Meta:
        model = AdCategory
        fields = (
            #'id',
            'url',
            'name_category',
            'date_created',
            'date_updated'
        )


## AD TAG SERIALIZERS ##
# Serializer for Ad LIST
class Ad_LIST_Serializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='ads-api:detailAD',
        lookup_field='id'
    )
    class Meta:
        model = Ad
        fields = (
            'user',
            'id',
            'url',
            'title',
            'description',
            #'slug',
            'priority',
            'location_country',
            'location_city',
            'location_postcode',
            'typeAd',
            'external',
            'external_link',
            'date_created',
            'date_updated',
            'date_external',
            'likes',
            'categories',
            'tags'
        )
# Serializer for Ad DETAIL
class Ad_DETAIL_Serializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = (
            'user',
            'id',
            #'url',
            'title',
            'description',
            #'slug',
            'priority',
            'location_country',
            'location_city',
            'location_postcode',
            'typeAd',
            'external',
            'external_link',
            'date_created',
            'date_updated',
            'date_external',
            'likes',
            'categories',
            'tags'
        )
# Serializer for Ad CREATE / UPDATE