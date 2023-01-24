from django.urls import path
from .views import (
    ProductCreateAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView
)

urlpatterns = [
    path('list/', ProductListAPIView.as_view(), name='product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('<int:id>/detail/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('<int:id>/update/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:id>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),
]