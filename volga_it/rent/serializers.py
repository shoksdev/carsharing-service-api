from rest_framework import serializers

from .models import Rent


class RentSerializer(serializers.ModelSerializer):
    """Сериализатор для обработки модели Аренды (Rent)"""

    class Meta:
        model = Rent
        fields = '__all__'
