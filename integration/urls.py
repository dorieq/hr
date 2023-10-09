from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartamentAPIView, LocationAPIView, EmployeeAPIView, PositionAPIView

urlpatterns = [
    path('departaments/', DepartamentAPIView.as_view(), name='departaments'),
    path('locations/', LocationAPIView.as_view(), name='locations'),
    path('employees/', EmployeeAPIView.as_view(), name='employees'),
    path('positions/', PositionAPIView.as_view(), name='positions'),
]
