from django.urls import path

from .views import (
    AdTagListAPIView,
    AdTagDetailAPIView,
    AdTagUpdateAPIView,
    AdTagDeleteAPIView
)

urlpatterns = [
    path('', AdTagListAPIView.as_view(), name='list-adtag'),
    path('<pk>', AdTagDetailAPIView.as_view(), name='detail-adtag'),
    path('<pk>/edit/', AdTagUpdateAPIView.as_view(), name='update-adtag'),
    path('<pk>/delete/', AdTagDeleteAPIView.as_view(), name='delete-adtag'),
]
