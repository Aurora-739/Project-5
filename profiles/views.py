# profiles/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from django.shortcuts import render, get_object_or_404
from .forms import NewsletterForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


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

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Thank you for subscribing to our newsletter!')
                return redirect('profiles:profile')
            except:
                messages.error(request, 'This email is already subscribed!')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # Pre-fill with user's info if logged in
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'name': request.user.get_full_name() or request.user.username,
                'email': request.user.email,
            }
        form = NewsletterForm(initial=initial_data)
    
    return render(request, 'profiles/newsletter_signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after signup
            return redirect('/')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})