from django.urls import path
from rest_framework.routers import DefaultRouter
from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonViewSet, SubscriptionAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'lessons', LessonViewSet, basename='lessons')

urlpatterns = [
                  # Эндпоинт для подписки
                  path('course/subscribe/', SubscriptionAPIView.as_view(), name='subscribe'),
              ] + router.urls  # Добавляем маршруты от роутера
