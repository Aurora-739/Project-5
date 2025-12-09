# checkout/models.py
import uuid
from django.db import models
from django.conf import settings
from products.models import Product  # assuming you have a Product model

class Order(models.Model):
    order_number = models.CharField(max_length=32, editable=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    address_line1 = models.CharField(max_length=80)
    address_line2 = models.CharField(max_length=80, blank=True, default='')
    postcode = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=40, default='')
    country = models.CharField(max_length=40, default='')
    
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    original_bag = models.TextField(null=False, blank=False, default='')

    def _generate_order_number(self):
        """Generate a random, unique order number"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """Update order total based on line items"""
        self.order_total = sum(item.lineitem_total for item in self.lineitems.all())
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.sku} on order {self.order.order_number}'
