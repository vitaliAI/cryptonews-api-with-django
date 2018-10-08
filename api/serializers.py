from rest_framework import serializers
from crypto.models import CryptoNews


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoNews

        fields = ('title',
                  'imageurl',
                  'body',
                  'source',
                  'source_url',
                  'source_id',
                  'sentiment')
