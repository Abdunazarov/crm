from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from apartment.serializers import ApartmentSerializer

from .models import Apartment


@api_view(['POST'])
def create_apartment(request):
    '''Yangi obyekt yaratish uchun API, obyektni rieltori avtomatik ravishda Http Headersda kevotgan userni (rieltorni) obyekt avtori qilib qo'yadi'''

    author = request.user

    apartment = Apartment(author=author)

    serialzier= ApartmentSerializer(apartment, data=request.data)

    if serialzier.is_valid():
        serialzier.save()
        return Response(serialzier.data)

    return Response(serialzier.errors)


@api_view(['GET'])
def get_apartments(request):
    '''Barcha obyektlarni get qilish uchun API'''
    all = Apartment.objects.all()
    serializer = ApartmentSerializer(all, many=True)

    return Response(serializer.data)
    


@api_view(['GET'])
def detail_apartment(request, pk):
    '''Yagona obyektni get qilish uchun API'''
    apartment = Apartment.objects.get(id=pk)
    serializer = ApartmentSerializer(apartment)

    return Response(serializer.data)


@api_view(['PUT'])
def update_apartment(request, pk):
    '''Obyektni update/edit/yangilash ucuhn API
    1) Obyektni faqatgina obyektni avtori va superadmin (admin stranitsasidan) update qila oladi'''
    apartment = Apartment.objects.get(id=pk)
    user = request.user

    if not apartment.author == user:
        return Response({'Error': 'You cannot edit this Apartment object'})
    
    serializer = ApartmentSerializer(instance=apartment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)



@api_view(['DELETE'])
def delete_apartment(request, pk):
    '''Obyektni bazadan o'chirish uchun API
    1) Obyektni faqatgina obyektni avtori, yani obyektni yaratgan rieltorgina va superadmin o'chira oladi'''

    apartment = Apartment.objects.get(id=pk)
    user = request.user
    data = {'Response': 'Could not delete the Apartment object'}

    if not apartment.author == user:
        return Response({'Error': 'You cannot edit this Apartment object'})
        
    if apartment.delete():
        data['Response'] = 'Apartment object deleted successfully'
    
    return Response(data)


