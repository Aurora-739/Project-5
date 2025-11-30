from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.contrib import messages
from django.http import JsonResponse



def add_to_bag(request, sku):
    product = get_object_or_404(Product, sku=sku)
    quantity = int(request.POST.get('quantity', 1))
    bag = request.session.get('bag', {})

    bag[sku] = bag.get(sku, 0) + quantity
    request.session['bag'] = bag
    messages.success(request, f'Added {product.name} to your bag')
    return redirect(request.POST.get('redirect_url', '/products'))


def view_bag(request):
    """A view to render the shopping bag contents"""
    bag = request.session.get('bag', {})
    products = []

    for sku, quantity in bag.items():  # change item_id -> sku
        product = get_object_or_404(Product, sku=sku)  # use sku instead of pk
        products.append({
            'product': product,
            'quantity': quantity,
            'subtotal': product.price * quantity  # calculate subtotal here
        })

    grand_total = sum(item['subtotal'] for item in products)

    context = {
        'bag_items': products,
        'grand_total': grand_total,
    }

    return render(request, 'bag/bag.html', context)


def adjust_bag(request, sku):
    """AJAX: Adjust quantity of a product in the bag and return new totals"""
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        bag = request.session.get('bag', {})

        if quantity > 0:
            bag[sku] = quantity
        else:
            bag.pop(sku, None)

        request.session['bag'] = bag

        # Calculate new subtotal and grand total
        product = get_object_or_404(Product, sku=sku)
        subtotal = product.price * quantity
        grand_total = 0
        for item_sku, qty in bag.items():
            p = Product.objects.get(sku=item_sku)
            grand_total += p.price * qty

        return JsonResponse({
            'success': True,
            'subtotal': f'{subtotal:.2f}',
            'grand_total': f'{grand_total:.2f}'
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)


def remove_from_bag(request, sku):
    bag = request.session.get('bag', {})

    try:
        del bag[sku]
        request.session['bag'] = bag
        return JsonResponse({'success': True})
    except KeyError:
        return JsonResponse({'error': 'Item not found'}, status=404)


def update_bag(request, sku):
    """Update quantity of the product in the bag"""
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        bag = request.session.get('bag', {})

        # Update quantity
        bag[sku] = quantity

        request.session['bag'] = bag
        messages.success(request, "Product quantity updated!")
        return redirect('view_bag')
    
    # bag/context.py
def bag_contents(request):
    bag_items = []
    grand_total = 0
    bag = request.session.get('bag', {})

    for sku, quantity in bag.items():
        product = Product.objects.get(sku=sku)
        subtotal = product.price * quantity
        grand_total += subtotal
        bag_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    context = {
        'bag_items': bag_items,
        'grand_total': grand_total
    }
    return context
