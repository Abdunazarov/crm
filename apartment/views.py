from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from apartment.serializers import ApartmentSerializer

from .models import Apartment


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_apartment(request):
    author = request.user

    apartment = Apartment(author=author)

    serialzier= ApartmentSerializer(apartment, data=request.data)

    if serialzier.is_valid():
        serialzier.save()
        return Response(serialzier.data)

    return Response(serialzier.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_apartments(request):
    all = Apartment.objects.all()
    serializer = ApartmentSerializer(all, many=True)

    return Response(serializer.data)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail_apartment(request, pk):
    apartment = Apartment.objects.get(id=pk)
    serializer = ApartmentSerializer(apartment)

    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_apartment(request, pk):
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
@permission_classes([IsAuthenticated])
def delete_apartment(request, pk):
    apartment = Apartment.objects.get(id=pk)
    user = request.user
    data = {'Response': 'Could not delete the Apartment object'}

    if not apartment.author == user:
        return Response({'Error': 'You cannot edit this Apartment object'})
        
    if apartment.delete():
        data['Response'] = 'Apartment object deleted successfully'
    
    return Response(data)


