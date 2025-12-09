from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after signup
            return redirect('/')  # Change 'home' to your desired redirect URL
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})