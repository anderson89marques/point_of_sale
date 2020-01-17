import uuid

from django.db import models

from point_of_sale.api.validators import (validate_name, validate_phone_number,
                                          validate_product_name)


class CreatedUpdated(models.Model):
    """Base model with create and update date information"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(CreatedUpdated):
    """Base model for person's base information"""
    name = models.CharField(max_length=100, validators=[
                            validate_product_name, validate_name])
    age = models.PositiveSmallIntegerField()
    phone = models.CharField(max_length=20, validators=[validate_phone_number])
    email = models.EmailField()


class Customer(Person):
    """Customer Model"""
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name


class Seller(Person):
    """Seller Model"""
    identify = models.UUIDField(default=uuid.uuid4)

    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = 'Sellers'

    def __str__(self):
        return self.name


class Product(CreatedUpdated):
    """Product Model"""
    name = models.CharField(max_length=100, validators=[
                            validate_product_name, validate_name], null=False, blank=False)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False)
    description = models.TextField(max_length=200, null=False, blank=False)
    minimum_stock = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Order(CreatedUpdated):
    """Order Model"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"<Order {self.id}>"


class OrderItem(CreatedUpdated):
    """Model that save information for a product sold in a order"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order, related_name='itens', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = 'OrderItens'

    def __str__(self):
        return f"<OrderItem name: {self.product.name}, price: {self.price}, quantity: {self.quantity}>"
