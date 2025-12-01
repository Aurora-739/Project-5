from django.shortcuts import render, redirect
from .forms import NewsletterForm


# Create your views here.
def newsletter_signup(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank_you")
    else:
        form = NewsletterForm()
    return render(request, "newsletter/signup.html", {"form": form})
