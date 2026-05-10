from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from users.views import PaymentListAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="Habits API",
        default_version='v1',
        description="Трекер полезных привычек",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('materials.urls', namespace='materials')),
    path('payments/', PaymentListAPIView.as_view(), name='payment-list'),
    path('habits/', include('habits.urls', namespace='habits')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
