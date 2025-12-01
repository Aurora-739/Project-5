# checkout/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product
from .models import Order, OrderLineItem
from .forms import OrderForm
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    bag = request.session.get('bag', {})

    if request.method == 'POST':
        # Gather form data from POST
        form_data = {
            'full_name': request.POST.get('full_name', ''),
            'email': request.POST.get('email', ''),
            'address_line1': request.POST.get('address_line1', ''),
            'address_line2': request.POST.get('address_line2', ''),
            'postcode': request.POST.get('postcode', ''),
            'city': request.POST.get('city', ''),
            'country': request.POST.get('country', ''),
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # Create order instance but do not save yet
            order = order_form.save(commit=False)

            # Attach user profile if logged in
            if request.user.is_authenticated:
                from profiles.models import UserProfile
                order.user_profile = UserProfile.objects.get(user=request.user)

            # Save order to DB
            order.save()

            # Create order line items
            for item_id, quantity in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity,
                        lineitem_total=product.price * quantity
                    )
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        "One of the products in your bag wasn't found in our database. "
                        "Please contact us for assistance."
                    )
                    order.delete()
                    return redirect('bag:view_bag')

            # Save info to session if requested
            request.session['save_info'] = 'save_info' in request.POST

            # Calculate grand total
            grand_total = sum(item.lineitem_total for item in order.lineitems.all())

            # Create Stripe PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=int(grand_total * 100),  # convert to pence
                currency='gbp',
                metadata={'order_number': order.order_number}
            )

            # Redirect to success page
            return redirect('checkout:checkout_success', order_number=order.order_number)

        else:
            messages.error(
                request,
                'There was an error with your form. Please double check your information.'
            )

    else:
        # GET request: show empty form
        order_form = OrderForm()
        # Create dummy PaymentIntent for Stripe Elements
        intent = stripe.PaymentIntent.create(
            amount=100,  # £1 dummy
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
        f'Order successfully processed! Your order number is {order_number}. '
        f'A confirmation email has been sent to {order.email}.'
    )

    # Clear shopping bag from session
    if 'bag' in request.session:
        del request.session['bag']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)


def payment_declined(request):
    return render(request, 'checkout/payment_declined.html')
