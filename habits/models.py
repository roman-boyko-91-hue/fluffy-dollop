from django.db import models
from django.conf import settings


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Создатель")
    place = models.CharField(max_length=255, verbose_name="Место")
    time = models.TimeField(verbose_name="Время выполнения")
    action = models.CharField(max_length=255, verbose_name="Действие")

    """Признак приятной привычки"""
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная привычка")

    """Связанная привычка (связка полезная + приятная)"""
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                      verbose_name="Связанная привычка")

    periodicity = models.PositiveSmallIntegerField(default=1, verbose_name="Периодичность (в днях)")
    reward = models.CharField(max_length=255, null=True, blank=True, verbose_name="Вознаграждение")
    time_to_complete = models.PositiveIntegerField(verbose_name="Время на выполнение (в секундах)")

    is_public = models.BooleanField(default=False, verbose_name="Публичная")

    def __str__(self):
        return f'{self.action} в {self.time} ({self.place})'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
