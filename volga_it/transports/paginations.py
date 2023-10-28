from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """Кастомная пагинация, выводит на страницу 3 объекта модели с возможностью увелечения количества до 30"""
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 30
