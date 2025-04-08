from rest_framework import serializers
from datetime import timedelta

from apps.reservation_service.models import Reservation
from apps.reservation_service.service import logger


class ReservationSerializer(serializers.ModelSerializer):
    """Default serializer for Reservation model"""
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        logger.info(f'Start validating reservation object: {data}')

        table = data['table_id']
        start_time = data['reservation_time']
        duration = data.get('duration_minutes')

        if duration is not None:
            end_time = start_time + timedelta(minutes=duration)
        else:
            end_time = None  # infinite

        logger.info(f'Got end time: {end_time}')

        existing_reservations = Reservation.objects.filter(table_id=table)

        for reservation in existing_reservations:
            res_start = reservation.reservation_time
            res_duration = reservation.duration_minutes
            res_end = None if res_duration is None else res_start + timedelta(minutes=res_duration)

            # Intersection check
            if end_time is None or res_end is None:
                # If at least one is infinite
                if (start_time <= res_end if res_end else True) and (res_start <= end_time if end_time else True):
                    raise serializers.ValidationError(
                        {"error": ["This table is already booked for an indefinite period of time."]}
                    )
            else:
                if start_time < res_end and res_start < end_time:
                    raise serializers.ValidationError({"error": ["This table is already booked for this time."]})

        logger.info(f'Validating reservation object successful')

        return data
