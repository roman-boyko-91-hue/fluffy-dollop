from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        send_mail(
            subject='Добро пожаловать!',
            message='Вы успешно зарегистрировались в нашем сервисе.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'users/login.html'
