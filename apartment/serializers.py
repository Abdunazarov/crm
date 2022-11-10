from .models import Apartment
from rest_framework import serializers


class ApartmentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    class Meta:
        model = Apartment
        fields = ('id', 'name', 'location', 'price', 'image', 'author')


