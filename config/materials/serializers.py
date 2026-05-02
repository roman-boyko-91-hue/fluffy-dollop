from rest_framework import serializers
from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # Поле для количества уроков
    lessons_count = serializers.SerializerMethodField()
    # Вложенный список уроков
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lessons_count', 'lessons')

    # Метод для подсчета уроков
    def get_lessons_count(self, instance):
        return instance.lessons.count()
