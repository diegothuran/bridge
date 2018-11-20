from rest_framework import generics
from .models import Relevancia_site
from .serializers import IndexSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class RelevanciaList(generics.ListCreateAPIView):
    queryset = Relevancia_site.objects.all()
    serializer_class = IndexSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('site',)
    filter_fields = '__all__'
    ordering_fields = '__all__'
