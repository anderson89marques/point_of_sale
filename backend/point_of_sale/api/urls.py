from django.urls import include, path
from rest_framework import routers

from point_of_sale.api import views

router = routers.DefaultRouter()
router.register('orders', views.OrderView, basename='order')
router.register('customers', views.CustomerView, basename='customer')
router.register('sellers', views.SellerView, basename='seller')
router.register('products', views.ProductView, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
