from rest_framework import serializers
from .models import Menu_Item

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu_Item
        fields = '__all__'