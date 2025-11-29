from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))  # default to 1 if not provided

    # Get the bag from the session, or create a new one if it doesn't exist
    bag = request.session.get('bag', {})

    if str(item_id) in bag:
        bag[str(item_id)] += quantity  # add to existing quantity
    else:
        bag[str(item_id)] = quantity  # add new item

    # Save the updated bag back to the session
    request.session['bag'] = bag

    return redirect('view_bag')  # redirect to the bag page

def view_bag(request):
    """A view to render the shopping bag contents"""
    bag = request.session.get('bag', {})
    products = []

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        products.append({
            'product': product,
            'quantity': quantity,
        })

    context = {
        'bag_items': products,
    }

    return render(request, 'bag/bag.html', context)
