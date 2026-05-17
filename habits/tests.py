from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit

User = get_user_model()


class HabitTestCase(APITestCase):
    def setUp(self):
        # Создаем основного пользователя и авторизуем его
        self.user = User.objects.create_user(
            email='test@test.com', password='password'
        )
        # Создаем второго пользователя для тестов прав доступа
        self.other_user = User.objects.create_user(
            email='other@test.com', password='password'
        )
        self.client.force_authenticate(user=self.user)

        # Базовая полезная привычка для тестов CRUD
        self.habit = Habit.objects.create(
            user=self.user,
            place="Дом",
            time="08:00:00",
            action="Зарядка",
            periodicity=1,
            time_to_complete=60
        )

        # Приятная привычка для тестов связанных привычек
        self.pleasant_habit = Habit.objects.create(
            user=self.user,
            place="Парк",
            time="19:00:00",
            action="Съесть фрукт",
            is_pleasant=True,
            periodicity=1,
            time_to_complete=30
        )

    def test_create_habit(self):
        """Тест успешного создания привычки"""
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

    def test_habit_list(self):
        """Тест: авторизованный пользователь видит только свои привычки"""
        # Создаем привычку чужого пользователя
        Habit.objects.create(
            user=self.other_user,
            place="Офис",
            time="14:00:00",
            action="Кофе-брейк",
            periodicity=1,
            time_to_complete=60
        )

        response = self.client.get('/habits/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # В результатах должна быть только 1 личная привычка (+ 1 приятная из setUp)
        self.assertEqual(len(response.json()['results']), 2)

    def test_public_habit_endpoint(self):
        """Тест: публичный эндпоинт отдает только публичные привычки"""
        # Делаем приятную привычку публичной
        self.pleasant_habit.is_public = True
        self.pleasant_habit.save()

        self.client.force_authenticate(user=None)
        response = self.client.get('/habits/public/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)
        self.assertEqual(
            response.json()['results'][0]['action'], "Съесть фрукт"
        )

    def test_habit_update_and_delete_owner(self):
        """Тест: владелец может изменять и удалять свою привычку"""
        # Тест PUT
        update_data = {
            "place": "Новый Дом",
            "time": "09:00:00",
            "action": "Зарядка",
            "periodicity": 2,
            "time_to_complete": 50
        }
        response = self.client.put(
            f'/habits/{self.habit.id}/', data=update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Тест DELETE
        response = self.client.delete(f'/habits/{self.habit.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_habit_permissions_other_user(self):
        """Тест: чужой пользователь не имеет доступа к чужой привычке"""
        self.client.force_authenticate(user=self.other_user)

        # Попытка просмотра
        response = self.client.get(f'/habits/{self.habit.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Попытка удаления
        response = self.client.delete(f'/habits/{self.habit.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_validator_time(self):
        """Тест: время выполнения не может быть больше 120 секунд"""
        data = {
            "place": "Зал", "time": "12:00:00", "action": "Бег",
            "periodicity": 1, "time_to_complete": 200
        }
        response = self.client.post('/habits/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "Время выполнения должно быть не больше 120 секунд.",
            response.json().get('non_field_errors', [])
        )

    def test_validator_reward_and_related_habit(self):
        """Тест: нельзя одновременно выбрать связанную привычку и награду"""
        data = {
            "place": "Дом", "time": "12:00:00", "action": "Чтение",
            "periodicity": 1, "time_to_complete": 60,
            "reward": "Шоколадка", "related_habit": self.pleasant_habit.id
        }
        response = self.client.post('/habits/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validator_related_habit_must_be_pleasant(self):
        """Тест: в связанные привычки могут попадать только приятные"""
        data = {
            "place": "Дом", "time": "12:00:00", "action": "Чтение",
            "periodicity": 1, "time_to_complete": 60,
            "related_habit": self.habit.id
        }
        response = self.client.post('/habits/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validator_pleasant_habit_restrictions(self):
        """Тест: у приятной привычки не может быть награды или связанной"""
        data = {
            "place": "Дом", "time": "12:00:00", "action": "Отдых",
            "is_pleasant": True, "periodicity": 1, "time_to_complete": 60,
            "reward": "Шоколадка"
        }
        response = self.client.post('/habits/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validator_periodicity(self):
        """Тест: периодичность не может быть реже, чем 1 раз в 7 дней"""
        data = {
            "place": "Дом", "time": "12:00:00", "action": "Уборка",
            "periodicity": 10, "time_to_complete": 60
        }
        response = self.client.post('/habits/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
