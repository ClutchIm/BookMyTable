import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from apps.reservation_service.service import create_table, create_reservation


@pytest.mark.django_db
def test_create_reservation_api():
    client = APIClient()
    table = create_table('Table 1')

    data = {
        "table_id": table.id,
        "customer_name": "Тест",
        "reservation_time": "2025-01-08T12:30:00Z",
        "duration_minutes": 30
    }

    url = reverse("reservations-list")
    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.data["message"] == "Reservation created successful"


@pytest.mark.django_db
def test_delete_reservation_api():
    client = APIClient()
    table = create_table('Table 1')
    reservation = create_reservation(table)

    url = reverse(f"reservations-detail", args=[reservation.id])
    response = client.delete(url)

    assert response.status_code == 204
    assert response.data["message"] == "Reservation deleted successful"


@pytest.mark.django_db
def test_get_reservation_api():
    client = APIClient()
    table = create_table('Table 1')
    reservation = create_reservation(table)

    url = reverse(f"reservations-detail", args=[reservation.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.data["id"] == reservation.pk
