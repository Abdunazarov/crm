from rest_framework.response import Response
from rest_framework.decorators import api_view

from request_buy.models import RequestBuy
from request_sell.models import RequestSell, ACTIVE, HOT, WARM

from .serializers import *


# ANALYTICS PAGE
@api_view(['GET'])
def analytics_count(request):
    '''Analitika stranitsasidagi, **(активные, горячиеб завершенные ва заявки без внимания)** zayavkalarni soni uchun chiqarilgan API, bu yerda response {"active_number: 45} ko'rinishida keladi"'''

    all_sell_active = RequestSell.objects.filter(status=ACTIVE).count()
    all_buy_active = RequestBuy.objects.filter(status=ACTIVE).count()
    all_active = all_buy_active + all_sell_active

    all_sell_hot = RequestSell.objects.filter(status=HOT).count()
    all_buy_hot = RequestBuy.objects.filter(status=HOT).count()
    all_hot = all_buy_hot + all_sell_hot

    all_sell_finished = RequestSell.objects.filter(finished=True).count()
    all_buy_finished = RequestBuy.objects.filter(finished=True).count()
    all_finished = all_sell_finished + all_buy_finished

    number_of_requests_with_no_attention = RequestBuy.objects.filter(no_attention=True).count() + RequestSell.objects.filter(no_attention=True).count()



    data = {
        'goryachiye': all_hot,
        'zavershonniye': all_finished,
        'bez_vnimaniya': number_of_requests_with_no_attention
    }

    if request.user.is_superuser:
        data['aktiv'] = all_active

    return Response(data)


# from itertools import chain
@api_view(['GET'])
def all_requests(request):
    '''Analitika stranitsasidagi'''


    all_requests = []

    requests_buy = RequestBuy.objects.all()
    requests_sell = RequestSell.objects.all()

    all_requests.extend(requests_buy)
    all_requests.extend(requests_sell)

    data = {
        'zayavka_prodaja': [],
        'zayavka_pokupka': []
    }

    for req in all_requests:

        if type(req) == type(RequestBuy()):
            serializer = RequestBuySerializer(req)
            data['zayavka_pokupka'].append(serializer.data)
        elif type(req) == type(RequestSell()):
            serializer = RequestBuySerializer(req)
            data['zayavka_prodaja'].append(serializer.data)


    return Response(data)


# CONTROL BEZ VNIMANIYA
