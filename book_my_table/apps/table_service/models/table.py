from django.db import models


class Table(models.Model):
    """
    A model representing a table in a restaurant.

    Used for booking and displaying available tables.
    """

    name = models.CharField(max_length=100, unique=True)
    seats = models.BigIntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
