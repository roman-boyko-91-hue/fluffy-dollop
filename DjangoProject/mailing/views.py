from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from .models import Client, Message, Mailing, MailingAttempt
from .services import send_mailing


# Главная страница
class HomeView(TemplateView):
    template_name = 'mailing/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            # Если это менеджер или админ — показываем общую статистику
            if user.groups.filter(name='Managers').exists() or user.is_superuser:
                mailings = Mailing.objects.all()
                clients_count = Client.objects.count()
                attempts = MailingAttempt.objects.all()
            else:
                # Если обычный юзер — только его данные
                mailings = Mailing.objects.filter(owner=user)
                clients_count = Client.objects.filter(owner=user).count()
                attempts = MailingAttempt.objects.filter(mailing__owner=user)

            context['total_mailings'] = mailings.count()
            context['active_mailings'] = mailings.filter(
                start_time__lte=timezone.now(),
                end_time__gte=timezone.now()
            ).count()

            context['unique_clients'] = clients_count

            # Статистика попыток
            context['success_attempts'] = attempts.filter(status='Успешно').count()
            context['fail_attempts'] = attempts.filter(status='Не успешно').count()
            context['total_messages_sent'] = attempts.count()  # Общее кол-во отправленных

        return context


# Клиенты (CRUD)
class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'full_name', 'comment')
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('email', 'full_name', 'comment')
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


# Сообщения (CRUD)
class MessageListView(ListView):
    model = Message

    def get_queryset(self):
        user = self.request.user
        # Менеджеры видят всё, обычные пользователи — только своё
        if user.groups.filter(name='Managers').exists() or user.is_superuser:
            return Mailing.objects.all()
        return Mailing.objects.filter(owner=user)


class MessageCreateView(CreateView):
    model = Message
    fields = ('subject', 'body')
    success_url = reverse_lazy('mailing:message_list')


# Рассылки (CRUD)
class MailingListView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('start_time', 'end_time', 'message', 'clients')
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MailingUpdateView(UserPassesTestMixin, UpdateView):
    model = Mailing

    def test_func(self):
        user = self.request.user
        # Редактировать может владелец, менеджер — НЕ может
        return self.get_object().owner == user or user.is_superuser


class MailingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')

    def test_func(self):
        # Удалять может только владелец или суперпользователь
        user = self.request.user
        return self.get_object().owner == user or user.is_superuser


# Ручной запуск
def force_send_mailing(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    result = send_mailing(mailing)

    if "error" in result:
        messages.error(request, f"Ошибка: {result['error']}")
    else:
        messages.success(request, "Рассылка успешно запущена!")

    return redirect(request.META.get('HTTP_REFERER', 'mailing:home'))


class AttemptListView(ListView):
    model = MailingAttempt
    template_name = 'mailing/attempt_list.html'

    def get_queryset(self):
        # Попытки только для рассылок текущего пользователя
        return MailingAttempt.objects.filter(mailing__owner=self.request.user)


@user_passes_test(lambda u: u.groups.filter(name='Managers').exists() or u.is_superuser)
def toggle_mailing_status(request, pk):
    """Функция для менеджеров: включить/выключить рассылку"""
    mailing = get_object_or_404(Mailing, pk=pk)
    mailing.is_active = not mailing.is_active  # Меняется True на False и наоборот
    mailing.save()
    return redirect('mailing:mailing_list')
