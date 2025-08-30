from django.db import models

# Create your models here.
class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    table_number = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=[("reserved", "Reserved"), ("cancelled", "Cancelled")],
        default="reserved"
    )

    def __str__(self):
        return f"Reservation {self.id} - Table {self.table_number} on {self.date}"