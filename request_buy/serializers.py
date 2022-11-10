from rest_framework import serializers
from .models import *



class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RequestBuy


class RequestUpdateSerializer(serializers.Serializer):
    status = serializers.BooleanField(required=False)
    name = serializers.CharField(required=False)
    data = serializers.DateTimeField(read_only=True, format="%Y-%m-%d (%X)")
    company_name = serializers.CharField(required=False)

    def update(self, data, instance):
        instance.status = data.get('status', instance.status)
        instance.name = data.get('name', instance.name)
        instance.company_name = data.get('company_name', instance.company_name)

        instance.save()
        return instance

