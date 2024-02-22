from django_filters import rest_framework as filters

from django.apps import apps
from django.contrib.auth import get_user_model

class LikeAnalyticsFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name='created_at', lookup_expr='gte')
    date_to = filters.DateFilter(field_name='created_at', lookup_expr='lte')
    
    class Meta:
        model = apps.get_model('posting.Like')
        fields = ['date', 'user']