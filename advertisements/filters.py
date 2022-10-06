from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter()
    updated_at = filters.DateFromToRangeFilter()
    creator = DjangoFilterBackend()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'updated_at', 'creator']
