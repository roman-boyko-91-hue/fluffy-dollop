from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from habits.models import Habit

User = get_user_model()


class HabitTestCase(APITestCase):
    def setUp(self):
        # Создаем пользователя
        self.user = get_user_model().objects.create_user(email='test@test.com', password='password')
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """Тест создания привычки и работы валидатора (время выполнения)"""
        data = {
            "place": "Дом",
            "time": "10:00:00",
            "action": "Выпить стакан воды",
            "is_pleasant": False,
            "periodicity": 1,
            "time_to_complete": 60
        }
        response = self.client.post('/habits/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_validator_time(self):
        """Тест: время выполнения не может быть больше 120 секунд"""
        data = {
            "place": "Зал",
            "time": "12:00:00",
            "action": "Бег",
            "is_pleasant": False,
            "periodicity": 1,
            "time_to_complete": 200  # Ошибка
        }
        response = self.client.post('/habits/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_habit_list(self):
        """Тест: пользователь видит только свои привычки"""

        Habit.objects.create(user=self.user, place="Улица", time="08:00:00", action="Прогулка", periodicity=1,
                             time_to_complete=60)

        response = self.client.get('/habits/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверяем, что в списке 1 запись
        self.assertEqual(len(response.json()['results']), 1)
