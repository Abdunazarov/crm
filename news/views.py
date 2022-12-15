from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import News
from .serializers import NewsSerializer

from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter


# CREATE
@api_view(['POST'])
def create_news(request):

    '''Yangiliklar yaratish uchun API, yangiliklarni faqat **rieltor** va **superadmin** yaratish imkoniga ega'''

    serializer = NewsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(request_data=request.data)
        return Response(serializer.data)

    return Response(serializer.errors)



# GET ONE
@api_view(['GET'])
def get_one_news(request, pk):

    '''Yagona yangilikni get qilish uchun API'''

    news = News.objects.get(id=pk)

    serializer = NewsSerializer(news)

    return Response(serializer.data)


# GET ALL
class ListNewsView(ListAPIView):
    '''Barcha yangiliklarni get qilish uchun API'''

    filter_backends = (SearchFilter,)
    search_fields = ('text',)

    queryset = News.objects.all()
    serializer_class = NewsSerializer



# UPDATE
@api_view(['PUT'])
def update_news(request, pk):
    '''Yangiliklarni update qilish uchun API, yangiliklarni faqat **rieltor** va **superadmin** update qilish imkoniga ega'''

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
def delete_news(request, pk):
    '''Yangiliklarni bazadan o'chirish uchun API, yangiliklarni faqat **rieltor** va **superadmin** o'chirish yuborish imkoniga ega'''

    news = News.objects.get(id=pk)
    data = {'Response': 'Failed to delete the news'}


    if news.delete():
        data['Response'] = 'Successfully deleted the news'

    return Response(data)


    


