"""
URL configuration for hr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auth.views import register, custom_login, custom_logout
from integration.views import DepartamentAPIView, LocationAPIView, EmployeeAPIView, PositionAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('departaments/', DepartamentAPIView.as_view(), name='departaments'),
    path('locations/', LocationAPIView.as_view(), name='locations'),
    path('employees/', EmployeeAPIView.as_view(), name='employees'),
    path('positions/', PositionAPIView.as_view(), name='positions'),
]
