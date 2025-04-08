import pytest

from apps.reservation_service.api import ReservationSerializer
from apps.reservation_service.models import Reservation
from apps.reservation_service.service import create_table, create_reservation, create_infinite_reservation, logger


@pytest.mark.django_db
def test_reservation_serializer_valid():
    table = create_table("Table 1")
    data = {
        "table_id": table.id,
        "customer_name": "Алексей",
        "reservation_time": "2025-05-08T21:00:00Z",
        "duration_minutes": 120
    }
    serializer = ReservationSerializer(data=data)

    assert serializer.is_valid(), serializer.errors


@pytest.mark.django_db
def test_reservation_serializer_table_exist():
    table = create_table("Table Test")
    exist_reservation = create_reservation(table)

    data = {
        "table_id": table.id,
        "customer_name": "Алексей",
        "reservation_time": exist_reservation.reservation_time,
        "duration_minutes": 120
    }
    serializer = ReservationSerializer(data=data)

    assert not serializer.is_valid(), serializer.errors
    assert serializer.errors["error"][0] == "This table is already booked for this time."


@pytest.mark.django_db
def test_reservation_serializer_infinite_reservation():
    table = create_table("Table Test")
    exist_reservation = create_infinite_reservation(table)

    data = {
        "table_id": table.id,
        "customer_name": "Алексей",
        "reservation_time": exist_reservation.reservation_time,
        "duration_minutes": 120
    }

    serializer = ReservationSerializer(data=data)

    assert not serializer.is_valid(), serializer.errors
    assert serializer.errors["error"][0] == "This table is already booked for an indefinite period of time."


