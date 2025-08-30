from django.shortcuts import render
from rest_framework import viewsets
from .models import Orders, Order_Item
from .serializers import OrderSerializer, OrderItemSerializer

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = Order_Item.objects.all()
    serializer_class = OrderItemSerializer