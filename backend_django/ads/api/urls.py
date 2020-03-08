from django.urls import path

from .views import (
    AdListAPIView,
    AdDetailAPIView,
    AdUpdateAPIView,
    AdDeleteAPIView
)

urlpatterns = [
    path('', AdListAPIView.as_view(), name='list'),
    path('<pk>', AdDetailAPIView.as_view(), name='detail'),
    path('<pk>/edit/', AdUpdateAPIView.as_view(), name='update'),
    path('<pk>/delete/', AdDeleteAPIView.as_view(), name='delete'),
]
