from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.table_service.service import logger
from apps.table_service.models import Table
from .serializers import TableSerializer


class TableViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing tables.

    Supports standard CRUD operations.
    """
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def create(self, request, *args, **kwargs):
        """Function that creates a new table."""
        logger.info(f'Start creating table with params: {request.data}')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f'Table created')
            return Response({"message": f"{serializer.data['name']} created successful"},
                            status=status.HTTP_201_CREATED)
        logger.info(f'Table don`t created: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """Function that deletes a table."""
        instance = self.get_object()
        logger.info(f'Deleting table: {instance}')
        name = instance.name
        self.perform_destroy(instance)
        return Response({"message": f"{name} is deleted"}, status=status.HTTP_204_NO_CONTENT)

