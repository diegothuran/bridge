from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Relevancia_site



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class IndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Relevancia_site
        fields = '__all__'

    def get_queryset(self):
        site = self.kwargs['site']
        return Relevancia_site.objects.filter(relevancia__site=site)
