from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import RegisterView, UserLoginView, ProfileView, confirm_email, reset_password

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('confirm-email/<str:token>/', confirm_email, name='confirm_email'),
    path('reset-password/', reset_password, name='reset_password'),
]
