from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class AdLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 1