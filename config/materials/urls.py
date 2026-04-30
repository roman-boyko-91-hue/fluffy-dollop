from django.urls import path
from rest_framework.routers import DefaultRouter
from .apps import MaterialsConfig
from .views import (CourseViewSet, LessonListAPIView, LessonCreateAPIView,
                    LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView)

app_name = MaterialsConfig.name

# Роутер для ViewSet курсов
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
                  # Пути для уроков (Generics)
                  path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
                  path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
              ] + router.urls  # Добавляем маршруты роутера
