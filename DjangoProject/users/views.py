import secrets

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib import messages

from .models import User


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.verification_token = secrets.token_hex(16)
        user.save()

        # Ссылка для письма
        host = self.request.get_host()
        url = f"http://{host}{reverse('users:confirm_email', args=[user.verification_token])}"

        send_mail(
            subject='Подтверждение почты',
            message=f'Для подтверждения регистрации перейдите по ссылке: {url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class ProfileView(UpdateView):
    model = User
    fields = ('email', 'avatar', 'phone', 'country')  # укажите поля из вашей модели
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def confirm_email(request, token):
    user = get_object_or_404(User, verification_token=token)
    user.is_active = True
    user.verification_token = None
    user.save()
    return redirect('users:login')

def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            new_password = secrets.token_hex(8)  # генерация нового пароля
            user.set_password(new_password)
            user.save()

            send_mail(
                subject='Сброс пароля',
                message=f'Ваш новый пароль для входа: {new_password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            messages.success(request, 'Новый пароль отправлен на вашу почту')
            return redirect(reverse('users:login'))
        else:
            messages.error(request, 'Пользователь с таким email не найден')

    return render(request, 'users/reset_password.html')
