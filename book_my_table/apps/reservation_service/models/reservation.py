from django.db import models
from apps.table_service.models.table import Table


class Reservation(models.Model):
    """
    Represents a reservation made by a user for a specific table and time.
    """
    customer_name = models.CharField(max_length=100)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reservations')
    reservation_time = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(null=True, blank=True) # null == infinite

    def __str__(self):
        return f"{self.customer_name} - {self.table_id}: {self.reservation_time}"
