from rest_framework import serializers
from .models import News



class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def save(self, request_data):
        news = News.objects.create(
            img=request_data.get('img'),
            text=request_data['text'],
        )
        return news

    def update(self, request_data, instance):
        instance.img = request_data.get('img', instance.img)
        instance.text = request_data.get('text', instance.text)

        instance.save()
        return instance


