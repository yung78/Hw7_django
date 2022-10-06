from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsPublisherOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    # Зачем отдельная функция если можно все прописать в permissions.py и запилить в permission_classes??????
    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "list":
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, IsPublisherOrReadOnly]
        return [permission() for permission in permission_classes]

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return Advertisement.objects.all()
        elif self.request.user.is_anonymous:
            return Advertisement.objects.exclude(status='DRAFT')
        else:
            return Advertisement.objects.filter(~Q(status='DRAFT') | Q(creator=self.request.user) & Q(status='DRAFT'))
