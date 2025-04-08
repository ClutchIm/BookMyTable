from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.reservation_service.api.views import ReservationViewSet


router = DefaultRouter()
router.register(r'', ReservationViewSet, basename='reservations')

urlpatterns = [
    path('', include(router.urls)),
]