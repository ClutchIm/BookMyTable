from apps.table_service.models import Table
from apps.reservation_service.models import Reservation


def create_table(name):
    return Table.objects.create(name=name, seats=4, location="Главный зал")

def create_reservation(table):
    reservation = Reservation.objects.create(
        table_id=table,
        customer_name="Иван",
        reservation_time="2025-04-08T19:00:00Z",
        duration_minutes=60
    )
    return reservation

def create_infinite_reservation(table):
    reservation = Reservation.objects.create(
        table_id=table,
        customer_name="Иван",
        reservation_time="2025-04-08T19:00:00Z"
    )
    return reservation
