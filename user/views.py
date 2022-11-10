from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializers import *
from .models import *

from request_buy.models import RequestBuy
from request_sell.models import RequestSell

# Create
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # coz only superuser can create Rieltors
def register_rieltor(request):
    data = {}

    user = request.user

    if user.is_superuser != True:
        return Response({'Error': 'You are not a superuser, thus cannot create a rieltor'})

    

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        data['email'] = user.email
        data['first_name'] = user.first_name
        data['second_name'] = user.second_name
        data['phone_number'] = user.phone_number
        data['password'] = request.data['password']
        data['token'] = Token.objects.get(user=user).key
        return Response(data)

    return Response(serializer.errors)


# GET PROFILE 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user

    all_requests_of_user = RequestSell.objects.filter(rieltor=user).count() + RequestBuy.objects.filter(rieltor=user).count()
    active_requests = RequestSell.objects.filter(rieltor=user, status='Активный').count() + RequestBuy.objects.filter(rieltor=user, status='Активный').count()
    hot_requests = RequestSell.objects.filter(rieltor=user, status='Горящий').count() + RequestBuy.objects.filter(rieltor=user, status='Горящий').count()
    warm_requests = RequestSell.objects.filter(rieltor=user, status='Завершенный').count() + RequestBuy.objects.filter(rieltor=user, status='Завершенный').count()
    # no_attention_requests = 


    data = {
        'first_name': user.first_name,
        'second_name': user.second_name,
        'email': user.email,
        'phone_number': user.phone_number,
        'role': user.role,
        'no_of_requests': all_requests_of_user,
        'no_of_active_requests': active_requests,
        'no_of_hot_requests': hot_requests,
        'no_of_warm_requests': warm_requests,
        # 'no_attention_requests': no_attention_requests
    }

    return Response(data)



# Update 
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user

    serializer = UserSerializer(user, data=request.data)

    if serializer.is_valid():
        serializer.update(request.data, instance=user)
        return Response(serializer.data)

    return Response(serializer.errors)




@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def all_users(request):
    users = User.objects.all()

    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)

