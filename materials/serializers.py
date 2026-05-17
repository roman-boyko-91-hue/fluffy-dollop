from rest_framework import serializers
from .models import Course, Lesson
from .validators import YoutubeOnlyValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        # Подключаем валидатор к полю video_link
        validators = [YoutubeOnlyValidator(field='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        validators = [YoutubeOnlyValidator(field='video_link')]


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
