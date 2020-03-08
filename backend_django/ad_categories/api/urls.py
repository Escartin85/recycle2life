from django.urls import path

from .views import (
    AdCategoryListAPIView,
    AdCategoryDetailAPIView,
    AdCategoryUpdateAPIView,
    AdCategoryDeleteAPIView
)

urlpatterns = [
    path('', AdCategoryListAPIView.as_view(), name='list-adcategory'),
    path('<pk>', AdCategoryDetailAPIView.as_view(), name='detail-adcategory'),
    path('<pk>/edit/', AdCategoryUpdateAPIView.as_view(), name='update-adcategory'),
    path('<pk>/delete/', AdCategoryDeleteAPIView.as_view(), name='delete-adcategory'),
]
