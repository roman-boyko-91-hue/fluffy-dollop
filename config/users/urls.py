from django.urls import path

from .views import UserCreateAPIView, PaymentCreateAPIView, PaymentListAPIView

app_name = 'users'

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-register'),
    path('payments/', PaymentListAPIView.as_view(), name='payments_list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
]
