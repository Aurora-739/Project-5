from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def mypage(request):
    return render(request, 'mypage.html')

def signup2(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')  # redirect wherever you want
    else:
        form = UserCreationForm()
    return render(request, 'signup2.html', {'form': form})

def login2(request):
    return render(request, 'login2.html')

def logout2(request):
    return render(request, 'logout2.html')