from rest_framework import serializers
from .models import Table, CustomUser

class TableSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Table
    fields = ('id', 'url', 'name', 'link')

class CustomUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('id', 'url', 'username', 'photo')