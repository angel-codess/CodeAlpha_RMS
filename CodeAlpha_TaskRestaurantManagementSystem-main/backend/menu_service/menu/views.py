from django.shortcuts import render
from rest_framework import viewsets
from .models import Menu_Item
from .serializers import MenuItemSerializer

# Create your views here.
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = Menu_Item.objects.all()
    serializer_class = MenuItemSerializer