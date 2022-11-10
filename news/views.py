from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import News
from .serializers import NewsSerializer

from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter


# CREATE
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_news(request):

    serializer = NewsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(request_data=request.data)
        return Response(serializer.data)

    return Response(serializer.errors)



# GET ONE
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_one_news(request, pk):
    news = News.objects.get(id=pk)

    serializer = NewsSerializer(news)

    return Response(serializer.data)


# GET ALL
class ListNewsView(ListAPIView):
    filter_backends = (SearchFilter,)
    search_fields = ('text',)

    queryset = News.objects.all()
    serializer_class = NewsSerializer

    # permission_classes = [IsAuthenticated, ]


# UPDATE
@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def update_news(request, pk):
    news = News.objects.get(id=pk)
    data = {'Response': 'Failed to update the news'}

    serializer = NewsSerializer(news, data=request.data)

    if serializer.is_valid():
        serializer.update(request_data=request.data, instance=news)
        data['Response'] = 'Successfully updated the news'
        return Response(data)

    return Response(data)


# DELETE
@api_view(['DELETE', 'GET'])
# @permission_classes([IsAuthenticated])
def delete_news(request, pk):
    news = News.objects.get(id=pk)
    data = {'Response': 'Failed to delete the news'}

    if news.delete():
        data['Response'] = 'Successfully deleted the news'

    return Response(data)


    
