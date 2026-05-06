import stripe
from django.conf import settings

# Подключаем ключ из настроек
stripe.api_key = settings.STRIPE_API_KEY


def create_stripe_product(name):
    """Создаем продукт в Stripe."""
    product = stripe.Product.create(name=name)
    return product.id


def create_stripe_price(amount, product_id):
    """Создаем цену в Stripe (сумма в рублях)."""
    price = stripe.Price.create(
        currency="rub",
        unit_amount=int(amount * 100),  # Переводим в копейки
        product=product_id,
    )
    return price.id


def create_stripe_session(price_id):
    """Создаем сессию оплаты и возвращаем ссылку."""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0",  # Возвращаем юзер после оплаты
        line_items=[{"price": price_id, "quantity": 1}],
        mode="payment",
    )
    return session.url, session.id
