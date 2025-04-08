from rest_framework import viewsets, status
from rest_framework.response import Response

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
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"{serializer.data['name']} created successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """Function that deletes a table."""
        instance = self.get_object()
        name = instance.name
        self.perform_destroy(instance)
        return Response({"message": f"{name} is deleted"}, status=status.HTTP_204_NO_CONTENT)

