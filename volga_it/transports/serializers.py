from rest_framework import serializers

from .models import Transports


class TransportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transports
        fields = '__all__'
