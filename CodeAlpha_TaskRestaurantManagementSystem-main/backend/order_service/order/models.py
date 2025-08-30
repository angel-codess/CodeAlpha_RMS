from django.db import models

# Create your models here.
class Orders(models.Model):
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"
    
class Order_Item(models.Model):
    order_id = models.IntegerField()
    menu_item_id = models.IntegerField()  # fetched from menu_service
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of Item {self.menu_item_id}"