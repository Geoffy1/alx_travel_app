# alx_travel_app/alx_travel_app/urls.py

from django.contrib import admin
from django.urls import path, include, re_path # Import re_path for regex paths
from rest_framework import permissions # For Swagger permissions
from drf_yasg.views import get_schema_view # For generating Swagger schema
from drf_yasg import openapi # For defining OpenAPI schema details

# Define API_INFO for Swagger documentation
API_INFO = openapi.Info(
    title="ALX Travel App API",
    default_version='v1',
    description="API documentation for the ALX Travel Listing Platform. "
                "This provides details on available endpoints, request/response formats, and authentication.",
    terms_of_service="https://www.google.com/policies/terms/", # Replace with your actual terms of service URL
    contact=openapi.Contact(email="contact@alxtravel.app"), # Replace with your project's contact email
    license=openapi.License(name="BSD License"), # Replace with your chosen license
)

# Schema view for Swagger
schema_view = get_schema_view(
    API_INFO,
    public=True,  # Set to False in production unless you want public API docs
    permission_classes=(permissions.AllowAny,), # Allow any user to view docs
)

urlpatterns = [
    path('admin/', admin.site.urls), # Django Admin interface

    # Include URLs from your 'listings' app
    # All URLs defined in listings/urls.py will be prefixed with 'listings/'
    path('listings/', include('listings.urls')), 

    # Swagger UI and ReDoc views for API documentation
    # JSON/YAML schema endpoints
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # Swagger UI endpoint
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # ReDoc UI endpoint
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
