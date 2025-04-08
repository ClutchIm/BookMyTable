from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.reservation_service.service import logger
from apps.reservation_service.models import Reservation
from .serializers import ReservationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing reservations.

    Supports standard CRUD operations.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        logger.info(f'Start creating reservation with params: {request.data}')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f'Finish creating reservation')
            return Response({"message": "Reservation created successful"}, status=status.HTTP_201_CREATED)
        logger.info(f'Failed creating reservation: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        logger.info(f'Deleting reservation: {instance}')
        self.perform_destroy(instance)
        return Response({"message": f"Reservation deleted successful"}, status=status.HTTP_204_NO_CONTENT)

