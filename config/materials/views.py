from rest_framework import viewsets, request
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Lesson, Subscription
from .paginators import MaterialsPagination
from .serializers import CourseSerializer, LessonSerializer
from .permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MaterialsPagination

    def get_permissions(self):
        """Определяет права доступа для разных действий."""
        if self.action == 'create':
            # Создавать может любой авторизованный, кроме модератора
            permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action in ['update', 'partial_update', 'retrieve', 'list']:
            # Просматривать и редактировать может модератор или владелец
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'destroy':
            # Удалять может только владелец
            permission_classes = [IsAuthenticated, IsOwner]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        # Если модератор — возвращаем все объекты
        if self.request.user.groups.filter(name='moderators').exists():
            return Course.objects.all()
        # Если обычный пользователь — только его собственные
        return Course.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """Автоматически сохраняет текущего пользователя как владельца."""
        serializer.save(owner=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = MaterialsPagination

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action in ['update', 'partial_update', 'retrieve', 'list']:
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        # Если модератор — возвращаем все объекты
        if self.request.user.groups.filter(name='moderators').exists():
            return Lesson.objects.all()
        # Если обычный пользователь — только его собственные
        return Lesson.objects.filter(owner=self.request.user)


class SubscriptionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course')
        course_item = get_object_or_404(Course, id=course_id)

        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'Подписка добавлена'

        return Response({"message": message})
