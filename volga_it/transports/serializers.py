from rest_framework import serializers

from .models import Transports


class TransportsSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Transports
        fields = '__all__'
