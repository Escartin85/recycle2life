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
from ads.models import Ad
from ads.api.serializers import AdSerializer


class AdListAPIView(ListAPIView):

    permission_classes = [IsAuthenticated]

    # GET REQUEST for LIST ADS
    def get(self, request, *args, **kwargs):
        # query about all object in the ADs DATABASE
        query = Ad.objects.all()
        # Serialize data of query in JSON format
        serializer = AdSerializer(query, many=True)
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
        return Response(serializer.errors)


class AdDetailAPIView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdUpdateAPIView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdDeleteAPIView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
