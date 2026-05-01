from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Payment
from .serializers import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    # Для фильтрации и сортировки
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    # Настройка поля для фильтрации
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)

    # Настройка поля для сортировки
    ordering_fields = ('payment_date',)
