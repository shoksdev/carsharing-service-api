from rest_framework import serializers

from .models import Transports


class TransportsSerializer(serializers.ModelSerializer):
    """Сериализатор, для работы с моделью Транспорта, в поле "owner" автоматически подставляется текущий пользователь"""
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Transports
        fields = '__all__'


class TransportsAdminSerializer(serializers.ModelSerializer):
    """Сериализатор, для работы с моделью Транспорта"""

    class Meta:
        model = Transports
        fields = '__all__'
