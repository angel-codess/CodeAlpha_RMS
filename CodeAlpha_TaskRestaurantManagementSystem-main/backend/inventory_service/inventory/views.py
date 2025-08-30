from django.shortcuts import render
from rest_framework import viewsets
from .models import Inventory
from .serializers import InventoryItemSerializer

# Create your views here.
class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventoryItemSerializer