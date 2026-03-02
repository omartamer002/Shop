from django.urls import path
from .views import ProductList, ProductDetail, VendorList, VendorDetail, ReviewViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
  path('products/', ProductList.as_view()),
  path('products/<int:pk>/', ProductDetail.as_view()),
  path('vendors/', VendorList.as_view()),
  path('vendors/<int:pk>/', VendorDetail.as_view()),
] + router.urls