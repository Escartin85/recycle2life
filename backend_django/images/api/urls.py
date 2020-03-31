from django.urls import path

from .views import (
    ImageListAPIView,
    ImageDetailAPIView,
    ImageUpdateAPIView,
    ImageDeleteAPIView,
    ImageCreateAPIView
)

app_name = 'images'
urlpatterns = [
    path('', ImageListAPIView.as_view(), name='listIMG'),
    path('<int:id>', ImageDetailAPIView.as_view(), name='detailIMG'),
    path('<int:id>/edit/', ImageUpdateAPIView.as_view(), name='updateIMG'),
    path('<int:id>/delete/', ImageDeleteAPIView.as_view(), name='deleteIMG'),
    path('create/', ImageCreateAPIView.as_view(), name='createIMG'),
]
