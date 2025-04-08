import pytest

from apps.table_service.api import TableSerializer


@pytest.mark.django_db
def test_table_serializer_valid():
    data = {
        "name": "Table Test",
        "seats": 4,
        "location": "Зал"
    }
    serializer = TableSerializer(data=data)

    assert serializer.is_valid(), serializer.errors
