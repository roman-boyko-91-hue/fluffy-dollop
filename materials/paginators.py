from rest_framework.pagination import PageNumberPagination


class MaterialsPagination(PageNumberPagination):
    page_size = 10  # Количество элементов на одной странице
    page_size_query_param = 'page_size'  # Позволяет клиенту самому выбрать размер страницы
    max_page_size = 100  # Максимальный лимит для клиента
