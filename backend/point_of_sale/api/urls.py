from django.urls import include, path
from point_of_sale.api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('orders', views.OrderView, basename='order')
router.register('customers', views.CustomerView, basename='customer')
router.register('sellers', views.SellerView, basename='seller')
router.register('products', views.ProductView, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
