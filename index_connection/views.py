from rest_framework import generics
from .models import Relevancia_site
from .serializers import IndexSerializer


class RelevanciaList(generics.ListCreateAPIView):
    queryset = Relevancia_site.objects.all()
    serializer_class = IndexSerializer

