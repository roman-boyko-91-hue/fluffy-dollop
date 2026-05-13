from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Habit
from .paginators import HabitPagination
from .serializers import HabitSerializer
from .permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    """
    Эндпоинт для работы с личными привычками пользователя.
    Доступен только авторизованным пользователям.
    """
    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        # Возвращаем привычки текущего авторизованного пользователя
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PublicHabitListView(generics.ListAPIView):
    """
    Эндпоинт для просмотра всех публичных привычек.
    Доступен любому пользователю.
    """
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [AllowAny]
