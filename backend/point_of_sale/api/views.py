from rest_framework import generics, viewsets

from point_of_sale.api.models import Customer, Order, Product, Seller
from point_of_sale.api.serializers import (CustomerSerializer,
                                           OrderCreateSerializer,
                                           OrderSerializer, ProductSerializer,
                                           SellerSerializer)


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class SellerView(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return OrderCreateSerializer
        return OrderSerializer
