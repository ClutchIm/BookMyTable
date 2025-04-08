from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.table_service.api.views import TableViewSet


router = DefaultRouter()
router.register(r'', TableViewSet, basename='tables')

urlpatterns = [
    path('', include(router.urls)),
]