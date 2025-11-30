from django.conf import settings
from decimal import Decimal
from products.models import Product


def bag_contents(request):
    bag_items = []
    grand_total = 0
    bag = request.session.get('bag', {})

    for sku, quantity in bag.items():
        try:
            product = Product.objects.get(sku=sku)
            subtotal = product.price * quantity
            grand_total += subtotal
            bag_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal
            })
        except Product.DoesNotExist:
            continue

    return {
        'bag_items': bag_items,
        'grand_total': grand_total
    }

