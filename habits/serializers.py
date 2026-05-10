from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('user',)

    def validate(self, data):
        """
        Валидация исключения одновременного выбора связанной привычки и вознаграждения.
        """
        if data.get('related_habit') and data.get('reward'):
            raise serializers.ValidationError(
                "Нельзя одновременно выбрать связанную привычку и вознаграждение."
            )

        # Валидация времени выполнения (не больше 120 секунд)
        if data.get('time_to_complete') and data.get('time_to_complete') > 120:
            raise serializers.ValidationError(
                "Время выполнения должно быть не больше 120 секунд."
            )

        return data
