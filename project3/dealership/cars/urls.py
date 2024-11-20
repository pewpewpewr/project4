from django.urls import path
from .views import CarAPIView

urlpatterns = [
    path('api/cars/', CarAPIView.as_view(), name='car-list-create'),
    path('api/cars/<int:pk>/', CarAPIView.as_view(), name='car-detail'),
]
