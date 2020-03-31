from django.urls import path, re_path

from .views import (
    AdListAPIView,
    AdDetailAPIView,
    #AdUpdateAPIView,
    #AdDeleteAPIView,
    AdCreateAPIView,
    # Ad Tag Views
    AdTagListAPIView,
    AdTagDetailAPIView,
    AdTagUpdateAPIView,
    AdTagDeleteAPIView,
    AdTagCreateAPIView,
    # Ad Category Views
    AdCategoryListAPIView,
    AdCategoryDetailAPIView,
    AdCategoryUpdateAPIView,
    AdCategoryDeleteAPIView,
    AdCategoryCreateAPIView
)

app_name = 'ads'
urlpatterns = [
    path('', AdListAPIView.as_view(), name='listAD'),
    path('<int:id>', AdDetailAPIView.as_view(), name='detailAD'),
    #path('<int:id>/edit/', AdUpdateAPIView.as_view(), name='ad-update'),
    #path('<int:id>/delete/', AdDeleteAPIView.as_view(), name='ad-delete'),
    path('create/', AdCreateAPIView.as_view(), name='ad-create'),
    # url fort AdTag
    path('ad_tags/', AdTagListAPIView.as_view(), name='listTAG'),
    path('ad_tags/<int:id>', AdTagDetailAPIView.as_view(), name='detailTAG'),
    #re_path(r'^ad_tags/(?P<id>[0-9])/edit/$', AdTagUpdateAPIView.as_view(), name='updateTAG'),  
    path('ad_tags/<int:id>/edit/', AdTagUpdateAPIView.as_view(), name='updateTAG'),
    path('ad_tags/<int:id>/delete/', AdTagDeleteAPIView.as_view(), name='deleteTAG'),
    path('ad_tags/create/', AdTagCreateAPIView.as_view(), name='createTAG'),
    # url for AdCategory
    path('ad_categories/', AdCategoryListAPIView.as_view(), name='listCAT'),
    path('ad_categories/<int:id>', AdCategoryDetailAPIView.as_view(), name='detailCAT'),
    path('ad_categories/<int:id>/edit/', AdCategoryUpdateAPIView.as_view(), name='updateCAT'),
    path('ad_categories/<int:id>/delete/', AdCategoryDeleteAPIView.as_view(), name='deleteCAT'),
    path('ad_categories/create/', AdCategoryCreateAPIView.as_view(), name='createCAT'),
]
