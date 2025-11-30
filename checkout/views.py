from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm
from .models import OrderLineItem
from products.models import Product

def checkout(request):
    # Get bag from session
    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect('products:all_products')  # adjust URL as needed

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            # Create line items from bag
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    quantity = item_data if isinstance(item_data, int) else item_data.get('quantity', 1)

                    line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity
                    )
                    line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, f"Product with ID {item_id} not found")
                    continue

            order.update_total()  # Update total after line items created
            messages.success(request, "Order successfully placed!")
            # Clear the bag after checkout
            request.session['bag'] = {}

            return redirect('products:all_products')  # or payment success page
    else:
        form = OrderForm()

    # Compute bag items and total for template
    bag_items = []
    grand_total = 0
    for item_id, item_data in bag.items():
        try:
            product = Product.objects.get(id=item_id)
            quantity = item_data if isinstance(item_data, int) else item_data.get('quantity', 1)
            subtotal = product.price * quantity
            grand_total += subtotal
            bag_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
            })
        except Product.DoesNotExist:
            continue

    context = {
        'form': form,
        'bag_items': bag_items,
        'grand_total': grand_total,
    }

    return render(request, 'checkout/checkout.html', context)
