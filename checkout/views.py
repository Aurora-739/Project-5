from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm
from .models import OrderLineItem, Order
from products.models import Product
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    bag = request.session.get('bag', {})
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect('products:all_products')

    # ------------------------------------
    # GET: Display checkout page
    # ------------------------------------
    if request.method != 'POST':
        form = OrderForm()

        bag_items = []
        grand_total = 0

        for item_id, item_data in bag.items():
            try:
                product = Product.objects.get(id=item_id)
            except Product.DoesNotExist:
                continue

            quantity = item_data if isinstance(item_data, int) else item_data.get('quantity', 1)
            subtotal = product.price * quantity
            grand_total += subtotal

            bag_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
            })

        grand_total_pence = int(grand_total * 100)

        try:
            intent = stripe.PaymentIntent.create(
                amount=grand_total_pence,
                currency='gbp',
                metadata={'bag': str(bag)},
            )
            client_secret = intent.client_secret
        except Exception:
            client_secret = None

        context = {
            'form': form,
            'bag_items': bag_items,
            'grand_total': grand_total,
            'stripe_public_key': stripe_public_key,
            'client_secret': client_secret,
        }

        return render(request, 'checkout/checkout.html', context)

    # ------------------------------------
    # POST: Create order
    # ------------------------------------
    form = OrderForm(request.POST)
    if form.is_valid():
        order = form.save(commit=False)

        # Save now so ID exists
        order.save()

        # Add line items
        for item_id, item_data in bag.items():
            try:
                product = Product.objects.get(id=item_id)
            except Product.DoesNotExist:
                messages.error(request, f"Product with ID {item_id} not found")
                continue

            quantity = item_data if isinstance(item_data, int) else item_data.get('quantity', 1)

            OrderLineItem.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )

        # Update order total
        order.update_total()
        order.save()

        # Clear bag
        request.session['bag'] = {}

        messages.success(request, "Order successfully placed!")
        return redirect('products:all_products')

    else:
        messages.error(request, "There was an error with the form")
        return redirect('checkout')
