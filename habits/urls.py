from django.urls import path
from rest_framework.routers import DefaultRouter

from .apps import HabitsConfig
from .views import HabitViewSet, PublicHabitListView

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r'', HabitViewSet, basename='habits')

urlpatterns = [
                  path('public/', PublicHabitListView.as_view(), name='public-habits'),
              ] + router.urls
