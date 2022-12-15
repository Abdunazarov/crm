from rest_framework import serializers
from request_buy.models import RequestBuy
from request_sell.models import RequestSell

from request_buy.serializers import RequestSerializer as RequestBuySerializer
from request_sell.serializers import RequestSerializer as RequestSellSerializer


from rest_framework.response import Response



class AllRequestsSerializer(serializers.Serializer):
    request_buy = RequestBuySerializer
    request_sell = RequestSellSerializer

    def display(self, req_buy, req_sell):
        buy_serializer = self.request_buy(req_buy, many=True)
        sell_serializer = self.request_sell(req_sell, many=True)

        return Response(buy_serializer)




    

        print(ls)