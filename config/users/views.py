from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .models import Payment, User
from .serializers import PaymentSerializer, UserSerializer
from .services import create_stripe_product, create_stripe_price, create_stripe_session


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


class PaymentCreateAPIView(CreateAPIView):
    # permission_classes = [AllowAny]

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):

        payment = serializer.save(user=self.request.user)

        # 2. Логика Stripe
        # Создаем продукт
        if payment.paid_course:
            product_name = payment.paid_course.title  # title!
        elif payment.paid_lesson:
            product_name = payment.paid_lesson.title  # title
        else:
            product_name = "Оплата обучения"
        product_id = create_stripe_product(product_name)

        # Создаем цену
        price_id = create_stripe_price(payment.amount, product_id)

        # Создаем сессию и получаем ссылку
        session_url, session_id = create_stripe_session(price_id)

        # 3. Сохраняем ссылку и ID сессии в модель платежа
        payment.session_id = session_id
        payment.link = session_url
        payment.save()
