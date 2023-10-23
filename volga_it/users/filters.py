from django_filters import rest_framework as filters

from users.models import CustomUser


class AccountAdminFilter(filters.FilterSet):
    start = filters.NumberFilter(field_name='id', lookup_expr='gte')

    class Meta:
        model = CustomUser
        fields = ['start', ]
