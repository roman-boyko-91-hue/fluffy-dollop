from django.contrib import admin
from django.urls import path, include

from users.views import PaymentListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('materials.urls', namespace='materials')),
    path('payments/', PaymentListAPIView.as_view(), name='payment-list'),
]
