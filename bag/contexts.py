from django.conf import settings
from decimal import Decimal

def bag_contents(request):
    """
    Makes the shopping bag available across all templates.
    """
    bag = request.session.get('bag', {})
    bag_items = []
    total = Decimal('0.00')
    product_count = 0

    for item_id, quantity in bag.items():
        # Get product info
        from products.models import Product
        product = Product.objects.get(pk=item_id)
        total += product.price * quantity
        product_count += quantity

        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'line_total': product.price * quantity,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': total,  # no delivery
    }

    return context
