from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product
from .models import Order, OrderLineItem
from .forms import OrderForm
from django.conf import settings
from .webhook_handler import StripeWH_Handler
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    bag = request.session.get('bag', {})

    if request.method == 'POST':
        # Gather form data
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()

            # Create order line items
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        # No sizes
                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            quantity=item_data
                        )
                    else:
                        # Items with sizes
                        for size, quantity in item_data['items_by_size'].items():
                            OrderLineItem.objects.create(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size
                            )
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please contact us for assistance."
                    ))
                    order.delete()
                    return redirect('bag:view_bag')

            # Save info to session if needed
            request.session['save_info'] = 'save_info' in request.POST

            # Create Stripe PaymentIntent
            # Convert grand_total to smallest currency unit (pence)
            grand_total = sum(
                (item.subtotal for item in order.lineitems.all())
            )
            intent = stripe.PaymentIntent.create(
                amount=int(grand_total * 100),
                currency='gbp',
                metadata={'order_number': order.order_number}
            )

            context = {
                'order_form': order_form,
                'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
                'client_secret': intent.client_secret,
                'order': order,
            }

            return render(request, 'checkout/checkout.html', context)

        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')

    else:
        # GET request: show empty form
        order_form = OrderForm()

        # Create a "dummy" PaymentIntent for GET to mount the card element
        intent = stripe.PaymentIntent.create(
            amount=100,  # £1 dummy amount
            currency='gbp',
        )

    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(
        request,
        f'Order successfully processed! Your order number is {order_number}. A confirmation email has been sent to {order.email}.'
    )

    # Delete shopping bag from session
    if 'bag' in request.session:
        del request.session['bag']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)


def payment_declined(request):
    return render(request, 'checkout/payment_declined.html')
