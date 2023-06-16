from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    # time_created = serializers.DateTimeField(format=' %d. %m. %Yг. в %H:%M')

    class Meta:
        model = News
        fields = ['title', 'text', 'author', 'time_created']
