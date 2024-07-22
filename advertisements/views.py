from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from django_filters import rest_framework as filters
from advertisements import filters as filters_advertisements



class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    permission_classes = [permissions.IsAuthor,]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = filters_advertisements.AdvertisementFilter

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтровq

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAuthenticated()]
        return []
