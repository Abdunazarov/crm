from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from request_buy.models import RequestBuy
from request_sell.models import RequestSell, ACTIVE, HOT, WARM


# ANALYTICS PAGE
@api_view(['GET'])
def count_active(request):
    all_sell = RequestSell.objects.filter(status=ACTIVE).count()
    all_buy = RequestBuy.objects.filter(status=ACTIVE).count()
    all_active = all_buy + all_sell
    return Response({'Number of ACTIVE requests': all_active})



@api_view(['GET'])
def count_hot(request):
    all_sell = RequestSell.objects.filter(status=HOT).count()
    all_buy = RequestBuy.objects.filter(status=HOT).count()
    all_active = all_buy + all_sell
    return Response({'Number of HOT requests': all_active})



@api_view(['GET'])
def count_warm(request):
    all_sell = RequestSell.objects.filter(status=WARM).count()
    all_buy = RequestBuy.objects.filter(status=WARM).count()
    all_active = all_buy + all_sell
    return Response({'Number of WARM requests': all_active})


# from itertools import chain
@api_view(['GET'])
def all_requests(request):
    pass
#     ls = []
#     requests_buy = RequestBuy.objects.all()
#     requests_sell = RequestSell.objects.all()


#     both_requests = list(chain(requests_sell, requests_buy))

#     return Response({"Response": ls})


# CONTROL BEZ VNIMANIYA

@api_view(['GET'])
def bez_vnimaniya(request):
    number_of_requests_with_no_attention = RequestBuy.objects.filter(no_attention=True).count() + RequestSell.objects.filter(no_attention=True).count()

    return Response({'Number of requests with no attention': number_of_requests_with_no_attention})


