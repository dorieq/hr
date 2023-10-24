from django.contrib import admin
from django.urls import path, include
from auth.views import get_all_users, get_user_by_itin, get_all_positions, get_all_locations,get_all_departments
from auth import views
from auth.views import registeruser
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API Description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('integration.urls')),
    path('api/register/', registeruser, name='register'),
    path('api/login/', views.loginuser, name='login'),
    path('api/users/', views.get_all_users, name='get-users'),
    path('api/user/<str:itin>/', get_user_by_itin, name='get_user_by_itin'),
    path('api/positions/', get_all_positions, name='get_all_positions'),
    path('api/locations/', get_all_locations, name='get_all_locations'),
    path('api/departments/', get_all_departments, name='get_all_departments'),
    path('api/positions/<int:position_id>/', views.get_position_by_id),
    path('api/departments/<int:department_id>/', views.get_department_by_id),
    path('api/locations/<int:location_id>/', views.get_location_by_id),
]




