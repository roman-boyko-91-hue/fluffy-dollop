from django.urls import path

from users.views import UserCreateAPIView

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-register'),
]


