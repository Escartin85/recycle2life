from django.urls import path

from .views import (
    ImageListAPIView,
    ImageDetailAPIView,
    ImageUpdateAPIView,
    ImageDeleteAPIView
)

urlpatterns = [
    path('', ImageListAPIView.as_view(), name='list-image'),
    path('<pk>', ImageDetailAPIView.as_view(), name='detail-image'),
    path('<pk>/edit/', ImageUpdateAPIView.as_view(), name='update-image'),
    path('<pk>/delete/', ImageDeleteAPIView.as_view(), name='delete-image'),
]
