from django.db import models

# Create your models here.
class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    #unit = models.CharField(max_length=20)  # e.g., "kg", "liters", "pcs"
    #last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} ({self.quantity})"