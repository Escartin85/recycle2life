# third party imports DRF
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated, 
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
# third party imports DJANGO
from django.utils import  timezone
# third party imports

# APP imports
from images.models import Image
from images.api.serializers import (
    Image_LIST_Serializer,
    Image_DETAIL_Serializer,
    Image_CREATEUPDATE_Serializer
)

# AD TAG VIEWS
# LIST ALL view
class ImageListAPIView(ListAPIView):

    #permission_classes = [IsAuthenticated]

    # set query for get all images filter by ordering date created
    def get_queryset(self):
        return Image.objects.all().order_by('date_created')

    # GET REQUEST for LIST ADS
    def get(self, request, *args, **kwargs):
        # query about all object in the ADs DATABASE
        query = Image.objects.all()
        # Serialize data of query in JSON format
        serializer = Image_LIST_Serializer(query, context={'request': request}, many=True)
        # return the data of query in JSON formant
        return Response(serializer.data, status=status.HTTP_200_OK)


# DETAIL single view
class ImageDetailAPIView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Image.objects.all()
    serializer_class = Image_DETAIL_Serializer
    permission_classes = [IsAuthenticated]
    

# UPDATE single view
class ImageUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Image.objects.all()
    serializer_class = Image_CREATEUPDATE_Serializer
    #permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # set query for get all images filter by ordering date created
    '''
    def get_queryset(self, id):
        return Image.objects.get(id=id)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
    # GET REQUEST for ONE IMAGE
    def get(self, request, id, *args, **kwargs):
        # query about get the object to modify or update
        query = self.get_queryset(id)
        # Serialize data of query in JSON format
        serializer = Image_LIST_Serializer(query, context={'request': request})
        # return the data of query in JSON formant
        return Response(serializer.data, status=status.HTTP_200_OK)
    '''
    # PUT REQUEST for update ONE IMAGE
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        print("----")
        print(instance)
        print(instance.id)
        print(instance.title)
        print(instance.format)
        print(instance.file)
        print(instance.date_created)
        print(instance.date_updated)
        print("========")
        print(request.data)
        print("title: ", request.data.get("title"))
        print("format: ", request.data.get("format"))
        print("file: ", request.data.get("file"))
        print("========>>>")
        
        if request.data.get("title") != '':
            instance.title = request.data.get("title")
        
        if request.data.get("format") != '':
            instance.format = request.data.get("format")
        
        if request.data.get("file") == '':
            instance.file = request.data.get("file")
            format = instance.file[:3]
            print(format)
        else:
            instance.file = request.data.get("file")
            format = instance.file[:3]
            print(format)
            
        instance.date_updated = timezone.now()
        '''
        print("========>>>-----")
        print(instance.id)
        print(instance.title)
        print(instance.format)
        print(instance.file)
        print(instance.date_created)
        print(instance.date_updated)
        print("========>>>-----")
        '''
        #serializer = self.get_serializer(instance, data=request.data)
        serializer = Image_CREATEUPDATE_Serializer(instance, data=request.data)
        print("======== serializer ===")
        print(serializer)
        print("======== data ===")
        #print(serializer.data)
        #serializer.is_valid(raise_exception=True)
        #self.perform_update(serializer)
        
        # Serialize data of query in JSON format
        #serializer = Image_LIST_Serializer(query, context={'request': request}, many=True)
        
        #serializer = Image_LIST_Serializer(data=request.data)
        
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # validate the serializer data
        #if serializer.is_valid():
            # save our data
            #serializer.save()
            # return the data of rquest in JSON formant
        #return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)
        # otherwise return serializer errors
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# DELETE single view
class ImageDeleteAPIView(DestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = Image_DETAIL_Serializer

# CREATE single view
class ImageCreateAPIView(CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = Image_CREATEUPDATE_Serializer
    permission_class = [IsAuthenticated, IsAdminUser]

    def create(self, request, *args, **kwargs):

        image = Image()
        image.title = request.data['title']
        image.format = request.data['format']
        image.file = request.data['file']
        image.date_created = timezone.now()
        image.date_updated = timezone.now()
        #return super().create(request, *args, **kwargs)
        image.save()
        return Response({"message": "Image entry successful"}, status=status.HTTP_201_CREATED)


    '''
    # POST REQUEST for LIST ADS
    def post(self, request, *args, **kwargs):
        # Serialize data of request in JSON format
        serializer = ImageSerializer(data=request.data)
        # validate the serializer data
        if serializer.is_valid():
            # save our data
            serializer.save()
            # return the data of rquest in JSON formant
            return Response(serializer.data)
        # otherwise return serializer errors
        return Response(serializer.errors)
    '''