from django.utils import timezone
from datetime import timedelta


def is_table_reserved(table):
    """
    Check a table reservation now

    :param table: Table object
    :return: boolean if table is reserved
    """
    now = timezone.now()
    reservations = table.reservations.all()
    for r in reservations:
        if r.duration_minutes is None:
            return True  # infinite
        end_time = r.reservation_time + timedelta(minutes=r.duration_minutes)
        if r.reservation_time <= now <= end_time:
            return True
    return False