from rest_framework import serializers
from apps.table_service.models import Table


class TableSerializer(serializers.ModelSerializer):
    """Default serializer for Table model"""
    class Meta:
        model = Table
        fields = '__all__'
