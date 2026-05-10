from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitListCreateAPIView, HabitPublicListAPIView, HabitRetrieveUpdateDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListCreateAPIView.as_view(), name='habit_list'),
    path('public/', HabitPublicListAPIView.as_view(), name='habit_public'),
    path('<int:pk>/', HabitRetrieveUpdateDestroyAPIView.as_view(), name='habit_detail'),
]
