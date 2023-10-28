from django_filters import rest_framework as filters

from .models import Transports


class TransportAdminFilter(filters.FilterSet):
    """Кастомный фильтр, используется для фильтрации транспорта по начальному числу выборки и типу транспорта"""
    start = filters.NumberFilter(field_name='id', lookup_expr='gte')
    transport_type_choice = filters.ChoiceFilter(field_name='transport_type', choices=Transports.TRANSPORT_TYPES)

    class Meta:
        model = Transports
        fields = ['start', 'transport_type_choice']
