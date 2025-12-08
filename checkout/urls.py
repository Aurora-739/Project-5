from django.urls import path
from . import views

app_name = 'checkout'  # ← this is required for namespacing

urlpatterns = [
    path('', views.checkout, name='checkout'),
]
