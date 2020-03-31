# third party imports DRF
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView
)
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated, 
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from rest_framework import status
# third party imports DJANGO
from django.utils import  timezone
from django.db.models import Q
# third party imports
from collections import defaultdict
# APP imports
from ads.models import Ad, AdTag, AdCategory
from ads.api.serializers import (
    Ad_LIST_Serializer,
    Ad_DETAIL_Serializer,
    #AdTag_CREATEUPDATE_Serializer,
    AdTag_LIST_Serializer,
    AdTag_DETAIL_Serializer,
    AdTag_CREATEUPDATE_Serializer,
    AdCategory_LIST_Serializer,
    AdCategory_DETAIL_Serializer,
    AdCategory_CREATEUPDATE_Serializer
)
from .permissions import IsOwnerOrReadOnly
from .pagination import AdLimitOffsetPagination

'''
# AD VIEWS

class AdListAPIView(ListAPIView):
    serializer_class = AdSerializer
    #permission_classes = [IsAuthenticated]

    # set query for get all ads filter by ordering date created
    def get_queryset(self):
        Ad.objects.all().order_by('-date_created')
    
    # GET REQUEST for LIST ADS
    def get(self, request, *args, **kwargs):
        #response = super().list(request, *args, **kwargs)
        # query about all object in the ADs DATABASE
        query = self.get_queryset()

        # query all categories for the ad
        all_categories = AdCategory.objects.filter(
            id__in=Ad.categories.through.objects.filter(
                ad__in=query).values('AdCategory_id')
                )
        category_names = {}

            #for category in all_categories:
            #    category_names[AdCategory.id] = category.name_category
            
            #categories_map = defaultdict(list)
            #for m2m in Ad.categories.through.objects.filter(ad__in=query):
            #    categories_map[m2m.ad_id].append(
            #        category_names[m2m.category_id]
            #    )

        #for each in response.data:
        #    each['categories'] = categories_map.get(each['id'], [])

        # Serialize data of query in JSON format
        serializer = AdSerializer(query, context={'request': request}, many=True)
        # return the data of query in JSON formant
        return Response(serializer.data)

    # POST REQUEST for LIST ADS
    def post(self, request, *args, **kwargs):
        # Serialize data of request in JSON format
        serializer = AdSerializer(data=request.data)
        # validate the serializer data
        if serializer.is_valid():
            # save our data
            serializer.save()
            # return the data of rquest in JSON formant
            return Response(serializer.data)
        # otherwise return serializer errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdDetailAPIView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdUpdateAPIView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdDeleteAPIView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

class AdCreateAPIView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def create(self, request, *args, **kwargs):

        ad = Ad()
        ad.title = request.data['title']
        ad.date_created = timezone.now()
        ad.date_updated = timezone.now()
        #return super().create(request, *args, **kwargs)
        #user = models.ForeignKey(User, on_delete=models.CASCADE)
        #title = models.CharField(max_length=150)
        #slug = models.SlugField(unique=True, blank=True)
        #description = models.TextField(max_length=1500)
        #priority = models.CharField(max_length=10)
        #location_country = models.CharField(max_length=50)
        #location_city = models.CharField(max_length=50)
        #location_postcode = models.CharField(max_length=10)
        #typeAd = models.CharField(max_length=10)
        #external = models.BooleanField(default=False, blank=True)
        #external_link = models.CharField(max_length=500, blank=True)
        #date_created = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
        #date_updated = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
        #date_external = models.DateTimeField(blank=True, null=True)
        #likes = models.PositiveIntegerField(
        #    validators=[MaxValueValidator(99999)], default=0, blank=True)
        # Relationships
        #categories = models.ManyToManyField(AdCategory)
        #tags = models.ManyToManyField(AdTag)
        #images = models.ManyToManyField(Image)
        ad.save()
        return Response({"message": "Ad entry successful"}, status=status.HTTP_201_CREATED)

# AD CATEGORY VIEWS

class AdCategoryListAPIView(APIView):

    #permission_classes = [IsAuthenticated]

    # GET REQUEST for LIST AD's CATEGORIES
    def get(self, request, *args, **kwargs):
        # query about all object in the ADs DATABASE order by "name_tag"
        #query = AdTag.objects.all().order_by('-date_created')
        query = AdCategory.objects.all().order_by('name_category')
        # Serialize data of query in JSON format
        serializer = AdCategorySerializer(query, context={'request': request}, many=True)
        # return the data of query in JSON formant
        return Response(serializer.data)

    # POST REQUEST for LIST ADS
    def post(self, request, *args, **kwargs):
        # Serialize data of request in JSON format
        serializer = AdCategorySerializer(data=request.data)
        # validate the serializer data
        if serializer.is_valid():
            # save our data
            serializer.save()
            # return the data of rquest in JSON formant
            return Response(serializer.data)
        # otherwise return serializer errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdCategoryDetailAPIView(RetrieveAPIView):
    queryset = AdCategory.objects.all()
    serializer_class = AdCategorySerializer


class AdCategoryUpdateAPIView(RetrieveAPIView):
    queryset = AdCategory.objects.all()
    serializer_class = AdCategorySerializer


class AdCategoryDeleteAPIView(RetrieveAPIView):
    queryset = AdCategory.objects.all()
    serializer_class = AdCategorySerializer

class AdCategoryCreateAPIView(CreateAPIView):
    queryset = AdTag.objects.all()
    serializer_class = AdTagSerializer

    def create(self, request, *args, **kwargs):

        tag = AdCategory()
        tag.name_tag = request.data['name_tag']
        tag.date_created = timezone.now()
        tag.date_updated = timezone.now()
        #return super().create(request, *args, **kwargs)
        tag.save()
        return Response({"message": "Ad's Category entry successful"}, status=status.HTTP_201_CREATED)

'''

# AD TAG VIEWS
# LIST ALL view
class AdTagListAPIView(ListAPIView):
    queryset = AdTag.objects.all().order_by('name_tag')
    serializer_class = AdTag_LIST_Serializer
    #permission_classes = [IsAuthenticated]

    # GET REQUEST for LIST AD's TAGS
    def get(self, request, *args, **kwargs):
        # query about all object in the ADs DATABASE order by "name_tag"
        #query = AdTag.objects.all().order_by('-date_created')
        query = AdTag.objects.all().order_by('name_tag')
        # Serialize data of query in JSON format
        serializer = AdTag_LIST_Serializer(query, context={'request': request}, many=True)
        # return the data of query in JSON formant
        return Response(serializer.data, status=status.HTTP_200_OK)

# DETAIL single view
class AdTagDetailAPIView(RetrieveAPIView):
    queryset = AdTag.objects.all()
    serializer_class = AdTag_DETAIL_Serializer
    lookup_field = 'id'

# UPDATE single view
class AdTagUpdateAPIView(RetrieveUpdateAPIView):
    queryset = AdTag.objects.all()
    serializer_class = AdTag_CREATEUPDATE_Serializer
    lookup_field = 'id'

# DELETE single view
class AdTagDeleteAPIView(DestroyAPIView):
    queryset = AdTag.objects.all()
    serializer_class = AdTag_DETAIL_Serializer
    lookup_field = 'id'

# CREATE single view
class AdTagCreateAPIView(CreateAPIView):
    queryset = AdTag.objects.all()
    serializer_class = AdTag_CREATEUPDATE_Serializer
    permission_classes = [IsAuthenticated, IsAdminUser]


# AD CATEGORY VIEWS
# LIST ALL view
class AdCategoryListAPIView(ListAPIView):
    queryset = AdCategory.objects.all().order_by('name_tag')
    serializer_class = AdCategory_LIST_Serializer
    
    #permission_classes = [IsAuthenticated]

    # GET REQUEST for LIST AD's CATEGORIES
    def get(self, request, *args, **kwargs):
        # query about all object in the ADs DATABASE order by "name_tag"
        #query = AdTag.objects.all().order_by('-date_created')
        query = AdCategory.objects.all().order_by('name_category')
        # Serialize data of query in JSON format
        serializer = AdCategory_LIST_Serializer(query, context={'request': request}, many=True)
        # return the data of query in JSON formant
        return Response(serializer.data)

# DETAIL single view
class AdCategoryDetailAPIView(RetrieveAPIView):
    queryset = AdCategory.objects.all()
    serializer_class = AdCategory_DETAIL_Serializer
    lookup_field = 'id'

# UPDATE single view
class AdCategoryUpdateAPIView(RetrieveUpdateAPIView):
    queryset = AdCategory.objects.all()
    serializer_class = AdCategory_CREATEUPDATE_Serializer

# DELETE single view
class AdCategoryDeleteAPIView(DestroyAPIView):
    queryset = AdCategory.objects.all()
    serializer_class = AdCategory_DETAIL_Serializer

# CREATE single view
class AdCategoryCreateAPIView(CreateAPIView):
    queryset = AdTag.objects.all()
    serializer_class = AdTag_CREATEUPDATE_Serializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def create(self, request, *args, **kwargs):

        tag = AdCategory()
        tag.name_tag = request.data['name_tag']
        tag.date_created = timezone.now()
        tag.date_updated = timezone.now()
        #return super().create(request, *args, **kwargs)
        tag.save()
        return Response({"message": "Ad's Category entry successful"}, status=status.HTTP_201_CREATED)
    

# AD VIEWS
# LIST ALL view
class AdListAPIView(ListAPIView):
    serializer_class = Ad_LIST_Serializer
    #queryset = Ad.objects.all().order_by('date_created')
    #permission_classes = [IsAuthenticated]
    pagination_class = AdLimitOffsetPagination

    # set query for get all ads filter by ordering date created
    def get_queryset(self):
        queryset_list = Ad.objects.all().order_by('date_created')
        query = self.request.GET.get("q")
        #return Ad.objects.all().order_by('date_created')
        return queryset_list
    
    # GET REQUEST for LIST ADS
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        # query about all object in the ADs DATABASE
        query = self.get_queryset()
        
        # query all categories for the ad
        all_categories = AdCategory.objects.filter(
            id__in=Ad.categories.through.objects.filter(
                ad__in=query).values('adcategory_id')
                )
        print("HOLA")
        category_names = {}
        print(all_categories)
        print("HOLA2")
        for category in all_categories:
            print("ID %s - CATEGORY: %s" % (category.id, category.name_category))
            category_names[category.id] = category.name_category
            print(category_names[category.id])
        print("CATEGORY NAMES:", category_names)
        print("--")
        categories_map = defaultdict(list)
        for m2m in Ad.categories.through.objects.filter(ad__in=query):
            print(m2m.id)
            print("%s, id=%s" % (category_names[m2m.adcategory_id], m2m.adcategory_id))
            categories_map[m2m.ad_id].append(
                category_names[m2m.adcategory_id]
            )
        print("--")
        print("~~CATEGORY NAMES:", category_names)
        print("--")
        for each in response.data:
            print()
            #each['categories'] = categories_map.get(each['id'], [])
            #print("EACH ONE: ", categories_map.get(int(each['id'], [])))
        
        print("RESPONSE: ", response.data)
        print("QUERy: ", query)
        print("REQUEST: ", request)
        # Serialize data of query in JSON format
        serializer = Ad_LIST_Serializer(query, context={'request': request}, many=True)
        # return the data of query in JSON formant
        #return Response(response.data)
        return Response(serializer.data)


# DETAIL single view
class AdDetailAPIView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = Ad_DETAIL_Serializer
    lookup_field = 'id'
    

# UPDATE single view
class AdUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = Ad_DETAIL_Serializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# DELETE single view
class AdDeleteAPIView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = Ad_DETAIL_Serializer

# CREATE single view
class AdCreateAPIView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = Ad_DETAIL_Serializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

'''
# POST REQUEST for LIST ADS
    def post(self, request, *args, **kwargs):
        # Serialize data of request in JSON format
        #serializer = AdTagSerializer(data=request.data, many=True)
        serializer = None
        
        # validate the serializer data
        if serializer.is_valid():
            # save our data
            serializer.save()
            # return the data of rquest in JSON formant
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # otherwise return serializer errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def create(self, request, *args, **kwargs):

        tag = AdTag()
        tag.name_tag = request.data['name_tag']
        tag.date_created = timezone.now()
        tag.date_updated = timezone.now()
        #return super().create(request, *args, **kwargs)
        tag.save()
        return Response({"message": "Ad's Tag entry successful"}, status=status.HTTP_201_CREATED)
'''