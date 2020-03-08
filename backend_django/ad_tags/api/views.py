# third party imports
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# APP imports
from ad_tags.models import AdTag
from ad_tags.api.serializers import AdTagSerializer


class AdTagListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    # GET REQUEST for LIST ADS
    def get(self, request, *args, **kwargs):
        # query about all object in the ADs DATABASE
        query = AdTag.objects.all()
        # Serialize data of query in JSON format
        serializer = AdTagSerializer(query, many=True)
        # return the data of query in JSON formant
        return Response(serializer.data)

    # POST REQUEST for LIST ADS
    def post(self, request, *args, **kwargs):
        # Serialize data of request in JSON format
        serializer = AdTagSerializer(data=request.data)
        # validate the serializer data
        if serializer.is_valid():
            # save our data
            serializer.save()
            # return the data of rquest in JSON formant
            return Response(serializer.data)
        # otherwise return serializer errors
        return Response(serializer.errors)


class AdTagDetailAPIView(RetrieveAPIView):
    queryset = AdTag.objects.all()
    serializer_class = AdTagSerializer


class AdTagUpdateAPIView(RetrieveAPIView):
    queryset = AdTag.objects.all()
    serializer_class = AdTagSerializer


class AdTagDeleteAPIView(RetrieveAPIView):
    queryset = AdTag.objects.all()
    serializer_class = AdTagSerializer
