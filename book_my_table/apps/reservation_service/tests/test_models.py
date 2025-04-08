import pytest
from apps.reservation_service.models import Reservation
from apps.reservation_service.service import create_table


@pytest.mark.django_db
def test_create_reservation_success():
    table = create_table("Table 1")

    reservation = Reservation.objects.create(
        table_id=table,
        customer_name="Иван",
        reservation_time="2025-04-08T19:00:00Z",
        duration_minutes=60
    )

    assert reservation.pk is not None
    assert reservation.customer_name == "Иван"