# checkout/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from products.models import Product
from .models import Order, OrderLineItem
from .forms import OrderForm
from django.conf import settings
from profiles.models import UserProfile
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    bag = request.session.get('bag', {})

    # Pre-fill form with user info if logged in
    profile = None
    if request.user.is_authenticated:
        profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
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
            order = order_form.save(commit=False)

            # Attach user profile if logged in
            if profile:
                order.user_profile = profile

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
                        "One of the products in your bag wasn't found in our database. Please contact us."
                    )
                    order.delete()
                    return redirect('bag:view_bag')

            # Save info to profile if "save info" checked
            request.session['save_info'] = 'save_info' in request.POST
            if profile and request.session['save_info']:
                profile.default_phone_number = request.POST.get('phone_number', '')
                profile.default_street_address1 = request.POST.get('address_line1', '')
                profile.default_street_address2 = request.POST.get('address_line2', '')
                profile.default_town_or_city = request.POST.get('city', '')
                profile.default_county = request.POST.get('county', '')
                profile.default_postcode = request.POST.get('postcode', '')
                profile.default_country = request.POST.get('country', '')
                profile.save()

            # Redirect to checkout success
            return redirect('checkout:checkout_success', order_number=order.order_number)

        else:
            messages.error(request, 'There was an error with your form. Please check your information.')

    else:
        # GET request: pre-fill form
        initial_data = {}
        if profile:
            initial_data = {
                'full_name': request.user.get_full_name(),
                'email': request.user.email,
                'address_line1': profile.default_street_address1,
                'address_line2': profile.default_street_address2,
                'postcode': profile.default_postcode,
                'city': profile.default_town_or_city,
                'country': profile.default_country,
            }

        order_form = OrderForm(initial=initial_data)

        # Dummy Stripe PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount=100,
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
    send_mail(
        subject=f"Order Confirmation - {order.order_number}",
        message=f"Thank you for your order!\n\n"
                f"Order Number: {order.order_number}\n"
                f"We will process your order and ship it shortly.\n\n"
                f"Thank you for shopping with us!",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[order.email],
        fail_silently=False,  # Set True if you don’t want errors to break the page
    )
    messages.success(
        request,
        f'Order successfully processed! Your order number is {order_number}. '
        f'A confirmation email has been sent to {order.email}.'
    )

    if 'bag' in request.session:
        del request.session['bag']

    context = {'order': order}
    return render(request, 'checkout/checkout_success.html', context)


def payment_declined(request):
    return render(request, 'checkout/payment_declined.html')
