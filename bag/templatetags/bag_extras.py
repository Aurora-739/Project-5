from django import template
from products.models import Product

register = template.Library()

@register.filter
def get_product(sku):
    """Return Product instance for a given SKU"""
    try:
        return Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        return None
