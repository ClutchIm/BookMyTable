import pytest
from apps.table_service.models import Table


@pytest.mark.django_db
def test_create_table_success():
    table = Table.objects.create(
        name="Table Test",
        seats=4,
        location="Near"
    )

    assert table.pk is not None
    assert table.seats == 4