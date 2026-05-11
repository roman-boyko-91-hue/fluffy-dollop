from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from .models import Habit
from .paginators import HabitPagination
from .serializers import HabitSerializer
from .permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.action == 'list':
            # возвращаем свои + публичные
            return Habit.objects.filter(
                Q(user=self.request.user) | Q(is_public=True)
            )
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
