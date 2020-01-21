"""Rest API Serialization Classes for point_of_sale project"""

from rest_framework import serializers

from point_of_sale.api.models import (Customer, Order, OrderItem, Product,
                                      Seller)


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """Handle Customer data"""
    class Meta: # pylint: disable=C0115
        model = Customer
        fields = ['id', 'name', 'age', 'email', 'phone']


class SellerSerializer(serializers.HyperlinkedModelSerializer):
    """Handle Seller data"""
    identify = serializers.UUIDField(read_only=True)

    class Meta: # pylint: disable=C0115
        model = Seller
        fields = ['id', 'name', 'age', 'email', 'phone', 'identify']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """Handle Seller data"""
    class Meta: # pylint: disable=C0115
        model = Product
        fields = ['id', 'name', 'description', 'price', 'minimum_stock', 'stock']


class OrderItemCreateSerializer(serializers.Serializer):
    """Handle OrderItem creational data"""
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)


class CustomerCreateSerializer(serializers.ModelSerializer):
    """Handle Customer creational data"""
    class Meta: # pylint: disable=C0115
        model = Customer
        fields = ['id', 'name']


class SellerCreateSerializer(serializers.ModelSerializer):
    """Handle Seller creational data"""
    class Meta: # pylint: disable=C0115
        model = Seller
        fields = ['id', 'name', 'identify']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """Handle Order data"""
    itens = OrderItemCreateSerializer(many=True, read_only=True)
    customer = CustomerSerializer(read_only=True)
    seller = SellerSerializer(read_only=True)

    class Meta: # pylint: disable=C0115
        model = Order
        fields = ['id', 'total_price', 'itens', 'customer', 'seller']


class OrderCreateSerializer(serializers.Serializer):
    """Handle Order creational data"""
    customer_id = serializers.IntegerField(write_only=True)
    customer = CustomerCreateSerializer(read_only=True)
    seller_id = serializers.IntegerField(allow_null=True, required=False)
    seller = SellerCreateSerializer(read_only=True)
    total_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    itens = OrderItemCreateSerializer(many=True)

    def create(self, validated_data):
        order_itens = validated_data.pop('itens', [])
        order = self._create_order(validated_data)
        self._create_itens(order, order_itens)
        return order

    def _create_order(self, validated_data):
        customer_id = validated_data.pop('customer_id')
        seller_id = validated_data.pop('seller_id', None)
        validated_data = {
            **validated_data,
            **{
                'customer': Customer.objects.get(pk=customer_id),
                'seller': seller_id if not seller_id else Seller.objects.get(pk=seller_id)
            }
        }
        order = Order.objects.create(**validated_data)
        return order

    def _create_itens(self, order, order_itens):
        for item in order_itens:
            pk = item.pop('id')
            product = Product.objects.get(pk=pk)
            order_item = OrderItem.objects.create(order=order, product=product, **item)
            order_item.calculate_commission()
