from django.urls import path, include

urlpatterns = [
    path('tables/', include('apps.table_service.urls')),
    path('reservations/', include('apps.reservation_service.urls')),
]