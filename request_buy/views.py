from urllib.robotparser import RequestRate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters

from request_buy.serializers import RequestSerializer, RequestUpdateSerializer
from .models import *

# GET ALL
class ListRequestsView(ListAPIView):
    queryset = RequestBuy.objects.all()
    serializer_class = RequestSerializer
    permission_classes = []

    filter_backends = (filters.SearchFilter,)
    search_fields = ['location', 'status', 'id']


# CREATE
@api_view(['POST'])
def create_request(request):

    serializer = RequestSerializer(data=request.data)

    if serializer.is_valid():
        obj = serializer.save()
        serializer = RequestSerializer(obj)
        return Response(serializer.data)

    return Response(serializer.errors)

# UPDATE
@api_view(['PUT'])
def update_request(request, pk):
    r = RequestBuy.objects.get(id=pk)
    data = {'Response': 'Error while updating Request'}
    serializer = RequestUpdateSerializer(r, data=request.data)

    if serializer.is_valid():
        serializer.update(request.data, r)
        data['Response'] = 'Request successfully updated!'
        return Response(data)

    return Response(data)


# DELETE
@api_view(['DELETE'])
def delete_request(request, pk):
    data = {'Response': 'Failed to delete'}
    r  = RequestBuy.objects.get(id=pk)

    if r.delete():
        data['Response'] = 'Deleted successfully'
        return Response(data)

    return Response(data)



# GET ONE
@api_view(['GET'])
def get_one_request(request, pk):
    r  = RequestBuy.objects.get(id=pk)

    serializer = RequestSerializer(r)

    return Response(serializer.data)
