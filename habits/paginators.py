from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    default_limit = 5
    max_limit = 50
