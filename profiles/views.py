# profiles/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from django.shortcuts import render, get_object_or_404


@login_required
def profile(request):
    """ Display and update the user's profile """
    profile = UserProfile.objects.get(user=request.user)
    orders = profile.orders.all()  # Related name from Order model

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profiles:profile')
        else:
            messages.error(request, 'Failed to update profile. Please check your info.')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,  # Used to hide bag info in success toasts
    }

    return render(request, 'profiles/profile.html', context)

def order_history(request, order_number):
    """ Display a past order """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, f'This is a past confirmation for order {order_number}.')

    context = {
        'order': order,
        'from_profile': True,  # Used in checkout success template
    }

    return render(request, 'checkout/checkout_success.html', context)
