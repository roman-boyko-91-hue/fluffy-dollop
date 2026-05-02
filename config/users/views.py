from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from .models import Payment, User
from .serializers import PaymentSerializer, UserSerializer


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    # Для фильтрации и сортировки
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    # Настройка поля для фильтрации
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)

    # Настройка поля для сортировки
    ordering_fields = ('payment_date',)


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
