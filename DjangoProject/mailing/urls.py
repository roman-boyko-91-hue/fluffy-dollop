from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import (
    HomeView,
    ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView,
    MessageListView, MessageCreateView,
    MailingListView, MailingCreateView,
    force_send_mailing, AttemptListView, MailingDeleteView, toggle_mailing_status
)

app_name = MailingConfig.name

urlpatterns = [
    # Главная со статистикой
    # Кешируем главную на 15 минут (900 секунд)
    path('', cache_page(900)(HomeView.as_view()), name='home'),

    # Клиенты
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    # Сообщения
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),

    # Рассылки
    path('mailings/', MailingListView.as_view(), name='mailing_list'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/send/<int:pk>/', force_send_mailing, name='force_send'),
    path('attempts/', AttemptListView.as_view(), name='attempt_list'),
    path('mailings/delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailings/toggle/<int:pk>/', toggle_mailing_status, name='toggle_status'),
]
