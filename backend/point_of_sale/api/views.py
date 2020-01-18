import datetime

from django.db.models import Sum, F
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from point_of_sale.api.models import (Customer, Order, OrderItem, Product,
                                      Seller)
from point_of_sale.api.serializers import (CustomerSerializer,
                                           OrderCreateSerializer,
                                           OrderSerializer, ProductSerializer,
                                           SellerSerializer)
from point_of_sale.api.utils import period_dates


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True)
    def products(self, request, *args, **kwargs):
        try:
            customer = self.get_object()
            start_date, end_date = period_dates(self.request.query_params)
            results = Product.objects.filter(
                orderitem__order__customer=customer, 
                orderitem__created_at__range=[start_date, end_date]) \
                .values('pk', 'name') \
                .annotate(created_at=F('orderitem__created_at'))
        except Exception as e:
            return Response({'error': e.__str__()})

        return Response(results)

class SellerView(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    @action(detail=True)
    def commission(self, request, *args, **kwargs):
        """Total commission's seller by date range"""

        seller = self.get_object()

        try:
            start_date, end_date = period_dates(self.request.query_params)
            orders = Order.objects.filter(
                seller__pk=seller.pk, created_at__range=[start_date, end_date])
            total_commission = sum(
                order.total_commission for order in orders.all())
        except Exception as e:
            return Response({'error': e.__str__()})

        return Response({'total_commission': total_commission, 'total_orders': orders.count()})


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False)
    def best_sellers(self, request, *args, **kwargs):
        """Best Sellers products by date range"""

        try:
            start_date, end_date = period_dates(self.request.query_params)
            results = Product.objects.filter(orderitem__created_at__range=[start_date, end_date]) \
                .annotate(total_sold=Sum('orderitem__quantity')) \
                .order_by('-orderitem__quantity') \
                .values('pk', 'name', 'total_sold')
        except Exception as e:
            return Response({'error': e.__str__()})

        return Response({'results': results})


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return OrderCreateSerializer
        return OrderSerializer
