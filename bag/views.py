from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.contrib import messages
from django.http import JsonResponse

def bag_contents(request):
    """Return bag items and totals"""
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
            continue  # skip missing products

    return {
        'bag_items': bag_items,
        'grand_total': grand_total
    }


def view_bag(request):
    context = bag_contents(request)
    return render(request, 'bag/bag.html', context)


def add_to_bag(request, sku):
    product = get_object_or_404(Product, sku=sku)
    quantity = int(request.POST.get('quantity', 1))
    bag = request.session.get('bag', {})

    bag[sku] = bag.get(sku, 0) + quantity
    request.session['bag'] = bag
    messages.success(request, f'Added {product.name} to your bag')
    return redirect(request.POST.get('redirect_url', '/products'))


def adjust_bag(request, sku):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        bag = request.session.get('bag', {})

        if quantity > 0:
            bag[sku] = quantity
        else:
            bag.pop(sku, None)

        request.session['bag'] = bag

        # Recalculate totals
        context = bag_contents(request)
        subtotal = next((item['subtotal'] for item in context['bag_items'] if item['product'].sku == sku), 0)

        return JsonResponse({
            'success': True,
            'subtotal': f'{subtotal:.2f}',
            'grand_total': f'{context["grand_total"]:.2f}'
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)


def remove_from_bag(request, sku):
    bag = request.session.get('bag', {})
    if sku in bag:
        del bag[sku]
        request.session['bag'] = bag
        messages.success(request, 'Item removed from bag')
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Item not found'}, status=404)


def update_bag(request, sku):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        bag = request.session.get('bag', {})

        if quantity > 0:
            bag[sku] = quantity
            messages.success(request, "Product quantity updated!")
        else:
            bag.pop(sku, None)
            messages.success(request, "Product removed from bag!")

        request.session['bag'] = bag
        return redirect('view_bag')
    

def view_bag(request):
    return render(request, 'bag/bag.html')
