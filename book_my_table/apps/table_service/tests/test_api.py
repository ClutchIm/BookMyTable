import pytest

from django.urls import reverse
from rest_framework.test import APIClient
from apps.reservation_service.service import create_table


@pytest.mark.django_db
def test_create_table_api():
    client = APIClient()

    data = {
        "name": "Table Test",
        "seats": 4,
        "location": "Зал"
    }

    url = reverse("tables-list")
    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.data["message"] == "Table Test created successful"


@pytest.mark.django_db
def test_delete_table_api():
    client = APIClient()
    table = create_table('Table Test')

    url = reverse(f"tables-detail", args=[table.id])
    response = client.delete(url)

    assert response.status_code == 204
    assert response.data["message"] == "Table Test is deleted"


@pytest.mark.django_db
def test_get_table_api():
    client = APIClient()
    table = create_table('Table Test')

    url = reverse(f"tables-detail", args=[table.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.data["id"] == table.pk
