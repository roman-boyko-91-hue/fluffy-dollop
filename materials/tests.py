from rest_framework.test import APITestCase
from rest_framework import status
from materials.models import Lesson, Course, Subscription
from users.models import User


class MaterialTestCase(APITestCase):

    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create(email="test@test.com")
        # Создаем тестовый курс
        self.course = Course.objects.create(title="Основы Django", owner=self.user)
        # Создаем тестовый урок
        self.lesson = Lesson.objects.create(
            title="Урок 1",
            course=self.course,
            owner=self.user,
            video_link="https://youtube.com"
        )
        # Авторизуем клиента сразу для всех тестов
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        """Тест создания урока с валидной ссылкой"""
        data = {
            "title": "Новый урок",
            "course": self.course.id,
            "video_link": "https://youtube.com"
        }
        response = self.client.post('/lessons/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_list(self):
        """Тест получения списка уроков"""
        response = self.client.get('/lessons/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscription_toggle(self):
        """Тест работы подписки (создание и удаление)"""
        data = {"course": self.course.id}

        # 1. Активируем подписку
        response = self.client.post('/course/subscribe/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Подписка добавлена")
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

        # 2. Удаляем подписку тем же запросом
        response = self.client.post('/course/subscribe/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Подписка удалена")
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())
